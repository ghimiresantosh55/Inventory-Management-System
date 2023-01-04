from decimal import Decimal

from django.db.models import OuterRef, Subquery, Sum, Count, DecimalField, Q
from django.db.models.functions import Coalesce

from src.item.models import Item


def get_remaining_sold_purchased_item_count(item_id: int) -> Item:
    asset_count = Item.objects.filter(pk=OuterRef("pk")).annotate(
        asset_count=Count(
            'purchasedetail__pu_pack_type_codes__pack_type_detail_codes__assetlist'
        )
    ).values('asset_count')

    purchase_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
        purchase_qty=Sum(
            'purchasedetail__qty',
            filter=Q(purchasedetail__purchase__purchase_type__in=[1, 3, 4])
        )
    ).values('purchase_qty')

    purchase_return_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
        purchase_return_qty=Sum(
            'purchasedetail__qty',
            filter=Q(purchasedetail__purchase__purchase_type__in=[2, 5])
        )
    ).values('purchase_return_qty')

    sale_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
        sale_qty=Sum(
            'saledetail__qty',
            filter=Q(saledetail__sale_master__sale_type=1)
        )
    ).values('sale_qty')

    sale_return_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
        sale_return_qty=Sum(
            'saledetail__qty',
            filter=Q(saledetail__sale_master__sale_type=2)
        )
    ).values('sale_return_qty')

    chalan_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
        chalan_qty=Sum(
            'chalandetail__qty',
            filter=Q(chalandetail__chalan_master__status=1)
        )
    ).values('chalan_qty')

    chalan_return_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
        chalan_return_qty=Sum(
            'chalandetail__qty',
            filter=Q(chalandetail__chalan_master__status=3)
        )
    ).values('chalan_return_qty')

    pending_customer_order_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
        pending_customer_order_qty=Sum(
            'orderdetail__qty',
            filter=Q(orderdetail__order__status=1)
        )
    ).values('pending_customer_order_qty')
    transfer_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
        transfer_qty=Sum('transferdetail__qty', filter=Q(transferdetail__transfer_master__transfer_type=1,
                                                         transferdetail__cancelled=False))
    ).values("transfer_qty")
    transfer_return_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
        transfer_return_qty=Sum('transferdetail__qty', filter=Q(transferdetail__transfer_master__transfer_type=2,
                                                                transferdetail__cancelled=False))
    ).values("transfer_return_qty")
    queryset = Item.objects.get(active=True, id=item_id).annotate(
        remaining_qty=Coalesce(
            Subquery(purchase_qty, output_field=DecimalField()), Decimal("0.00")
        ) - Coalesce(
            Subquery(purchase_return_qty, output_field=DecimalField()), Decimal("0.00")
        ) - Coalesce(
            Subquery(sale_qty, output_field=DecimalField()), Decimal("0.00")
        ) + Coalesce(
            Subquery(sale_return_qty, output_field=DecimalField()), Decimal("0.00")
        ) - Coalesce(
            Subquery(pending_customer_order_qty, output_field=DecimalField()), Decimal("0.00")
        ) - Subquery(
            asset_count, output_field=DecimalField()
        ) - Coalesce(
            Subquery(chalan_qty, output_field=DecimalField()), Decimal("0.00")
        ) + Coalesce(
            Subquery(chalan_return_qty, output_field=DecimalField()), Decimal("0.00")
        ) - Coalesce(
            Subquery(transfer_qty, output_field=DecimalField()), Decimal("0.00")
        ) + Coalesce(
            Subquery(transfer_return_qty, output_field=DecimalField()), Decimal("0.00")
        )

    ).values(
        'id', 'purchase_cost', 'sale_cost', 'name', 'discountable',
        'taxable', 'tax_rate', 'code', 'item_category',
        'remaining_qty'
    )

    return queryset
