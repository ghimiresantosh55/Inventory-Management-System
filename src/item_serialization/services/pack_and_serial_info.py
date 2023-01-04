from django.db.models import OuterRef, F, Count, Exists

from src.item_serialization.models import PackingTypeCode, PackingTypeDetailCode


def find_available_pack(purchase_detail_id: int = None) -> PackingTypeCode.objects.none():
    pack_type_detail = PackingTypeDetailCode.objects.filter(
        assetlist__isnull=True,
        pack_type_code=OuterRef("id"),
        packingtypedetailcode__isnull=True
    ).annotate(
        ref_count=Count('pack_type_detail_code_of_sale') % 2
    ).filter(ref_count=0)

    if purchase_detail_id is not None:

        queryset = PackingTypeCode.objects.filter(purchase_detail=purchase_detail_id).annotate(
            location_code=F('location__code'),
            packet_available=Exists(pack_type_detail)
        ).filter(packet_available=True, location__isnull=False).values("id", "location_code", "code")

    else:

        queryset = PackingTypeCode.objects.annotate(
            location_code=F('location__code'),
            packet_available=Exists(pack_type_detail),
            batch_no=F('purchase_detail__batch_no'),
            item_id=F('purchase_detail__item_id'),
            item_name=F('purchase_detail__item__name')

        ).filter(packet_available=True, location__isnull=False).values("id", "location_code",
                                                                       "code", "batch_no",
                                                                       "purchase_detail", "item_id", "item_name")

    return queryset


def find_available_serial_nos(pack_id: int = None) -> PackingTypeDetailCode.objects.none():
    pack_type_detail = PackingTypeDetailCode.objects.filter(
        assetlist__isnull=True,
        id=OuterRef("id"),
        packingtypedetailcode__isnull=True
    ).annotate(
        ref_count=Count('pack_type_detail_code_of_sale') % 2
    ).filter(ref_count=0)

    if pack_id is not None:
        queryset = PackingTypeDetailCode.objects.filter(pack_type_code=pack_id).annotate(
            packet_available=Exists(pack_type_detail)
        ).filter(packet_available=True, pack_type_code__location__isnull=False).values("id", "code")
    else:
        queryset = PackingTypeDetailCode.objects.annotate(
            packet_available=Exists(pack_type_detail),
            batch_no=F('pack_type_code__purchase_detail__batch_no'),
            purchase_detail=F('pack_type_code__purchase_detail'),
            item_id=F('pack_type_code__purchase_detail__item_id'),
            item_name=F('pack_type_code__purchase_detail__item__name'),
        ).filter(packet_available=True, pack_type_code__location__isnull=False).values("id", "code", "pack_type_code",
                                                                                       "batch_no",
                                                                                       "purchase_detail", "item_id",
                                                                                       "item_name")

    return queryset


def find_available_serial_no(serial_no: str) -> bool:
    return PackingTypeDetailCode.objects.filter(
        assetlist__isnull=True,
        code=serial_no,
        packingtypedetailcode__isnull=True
    ).annotate(
        ref_count=Count('pack_type_detail_code_of_sale') % 2
    ).filter(ref_count=0).exists()


def find_available_pack_in_item(item_id: int = None) -> PackingTypeCode.objects.none():
    pack_type_detail = PackingTypeDetailCode.objects.filter(
        assetlist__isnull=True,
        pack_type_code=OuterRef("id"),
        packingtypedetailcode__isnull=True
    ).annotate(
        ref_count=Count('pack_type_detail_code_of_sale') % 2
    ).filter(ref_count=0)

    queryset = PackingTypeCode.objects.filter(purchase_detail__item=item_id).annotate(
        location_code=F('location__code'),
        packet_available=Exists(pack_type_detail)
    ).filter(packet_available=True, location__isnull=False).values("id", "location_code", "code")

    return queryset


def find_available_item_serial_nos(item_id: int) -> bool:
    return PackingTypeDetailCode.objects.filter(
        assetlist__isnull=True,
        pack_type_code__purchase_detail__item=item_id,
        packingtypedetailcode__isnull=True
    ).annotate(
        ref_count=Count('pack_type_detail_code_of_sale') % 2
    ).filter(ref_count=0).values("id", "code", "pack_type_code")
