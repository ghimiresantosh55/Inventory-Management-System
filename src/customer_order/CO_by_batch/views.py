from decimal import Decimal

import django_filters
from django.db import transaction
from django.db.models import OuterRef, Subquery, Sum, F, DecimalField, Count
from django.db.models.functions import Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from src.chalan.models import ChalanDetail
from src.customer_order.models import OrderDetail
from src.customer_order.models import OrderMaster
from src.item_serialization.services import pack_and_serial_info
from src.purchase.models import PurchaseDetail
from src.sale.models import SaleDetail
from .list_serializers import GetStockByBatchListSerializer, GetPackTypeDetailByBatchSerializer, \
    GetPackTypeByBatchSerializer
from .serializers import (SaveCustomerOrderByBatchSerializer,
                          SaveAndVerifyCustomerPackingTypesSerializer, UpdateCustomerOrderByBatchSerializer,
                          UpdateCustomerDetailsByBatchSerializer)
from ...item.models import Item
from ...item_serialization.models import PackingTypeCode
from ...transfer.models import TransferDetail


class ByBatchItemListFilter(django_filters.FilterSet):
    item = django_filters.ModelMultipleChoiceFilter(queryset=Item.objects.filter(active=True),
                                                    to_field_name='id')
    exclude_id = django_filters.ModelMultipleChoiceFilter(queryset=PurchaseDetail.objects.
                                                          filter(ref_purchase_detail__isnull=True),
                                                          to_field_name='id', exclude=True)

    class Meta:
        model = PurchaseDetail
        fields = ['item', 'id', 'exclude_id']


class GetStockByBatchListViewSet(ListAPIView):
    filter_backends = (OrderingFilter, SearchFilter, DjangoFilterBackend)
    search_fields = ['batch_no']
    ordering_fields = ['id']
    filter_class = ByBatchItemListFilter
    serializer_class = GetStockByBatchListSerializer

    def get_queryset(self):
        asset_count = PurchaseDetail.objects.filter(pk=OuterRef("pk"), ref_purchase_detail__isnull=True).annotate(
            asset_count=Count(
                'pu_pack_type_codes__pack_type_detail_codes__assetlist'
            )
        ).values('asset_count')
        purchase_return_qty = PurchaseDetail.objects.filter(ref_purchase_detail=OuterRef("pk")).values(
            "ref_purchase_detail"
        ).annotate(
            purchase_return_qty=Sum(
                'qty',
                output_field=DecimalField()
            )
        ).values('purchase_return_qty')

        sale_qty = SaleDetail.objects.filter(ref_purchase_detail=OuterRef("pk"), sale_master__sale_type=1).values(
            "ref_purchase_detail").annotate(
            sale_qty=Sum(
                'qty'
            )
        ).values('sale_qty')

        transfer_qty = TransferDetail.objects.filter(
            ref_purchase_detail=OuterRef("pk"), transfer_master__transfer_type=1, cancelled=False
        ).values("ref_purchase_detail").annotate(
            transfer_qty=Sum('qty')
        ).values("transfer_qty")
        transfer_return_qty = TransferDetail.objects.filter(
            ref_purchase_detail=OuterRef("pk"), transfer_master__transfer_type=2, cancelled=False
        ).values("ref_purchase_detail").annotate(
            transfer_return_qty=Sum('qty')
        ).values("transfer_return_qty")

        sale_return_qty = SaleDetail.objects.filter(
            ref_purchase_detail=OuterRef("pk"), sale_master__sale_type=2, sale_master__return_dropped=True).annotate(
            sale_return_qty=Sum(
                'qty'
            )
        ).values('sale_return_qty')

        chalan_qty = ChalanDetail.objects.filter(
            ref_purchase_detail=OuterRef("pk"), chalan_master__status=1
        ).values("ref_purchase_detail").annotate(
            chalan_qty=Sum(
                'qty'
            )
        ).values('chalan_qty')

        chalan_return_qty = ChalanDetail.objects.filter(
            ref_purchase_detail=OuterRef("pk"), chalan_master__status=3, chalan_master__return_dropped=True
        ).values("ref_purchase_detail").annotate(
            chalan_return_qty=Sum(
                'qty'
            )
        ).values('chalan_return_qty')

        pending_customer_order_qty = OrderDetail.objects.filter(
            purchase_detail=OuterRef("pk"), order__status=1, cancelled=False
        ).values("purchase_detail").annotate(
            pending_customer_order_qty=Sum(
                'qty'
            )
        ).values('pending_customer_order_qty')

        queryset = PurchaseDetail.objects.filter(
            ref_purchase_detail__isnull=True
        ).annotate(
            remaining_qty=
            F('qty')
            - Coalesce(
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

        ).filter(remaining_qty__gt=0).values("id", "batch_no", "qty",
                                             "remaining_qty", "purchase_cost")

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(queryset, status=status.HTTP_200_OK)


class GetPackTypeByBatchFilterSet(django_filters.FilterSet):
    location_code = django_filters.CharFilter(field_name='location__code')

    class Meta:
        model = PackingTypeCode
        fields = ['purchase_detail', 'location_code']


class GetPackTypeByBatchRetrieveApiView(ListAPIView):
    filter_backends = (DjangoFilterBackend,)
    filter_class = GetPackTypeByBatchFilterSet
    serializer_class = GetPackTypeByBatchSerializer

    def get_queryset(self):
        queryset = pack_and_serial_info.find_available_pack()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(queryset, status=status.HTTP_200_OK)


class GetPackTypeDetailByBatchRetrieveApiView(ListAPIView):
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['pack_type_code', 'code']
    serializer_class = GetPackTypeDetailByBatchSerializer

    def get_queryset(self):
        queryset = pack_and_serial_info.find_available_serial_nos()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(queryset, status=status.HTTP_200_OK)


class SaveCustomerOrderByBatchApiView(CreateAPIView):
    serializer_class = SaveCustomerOrderByBatchSerializer
    queryset = OrderMaster.objects.all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super(SaveCustomerOrderByBatchApiView, self).create(request, *args, **kwargs)


class SaveAndVerifyCustomerPackingTypesApiView(CreateAPIView):
    serializer_class = SaveAndVerifyCustomerPackingTypesSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = SaveAndVerifyCustomerPackingTypesSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCustomerOrderByBatchAPIView(UpdateAPIView):
    queryset = OrderMaster.objects.filter(status=1, by_batch=True).select_related('customer',
                                                                                  'discount_scheme').prefetch_related(
        'order_details')
    serializer_class = UpdateCustomerOrderByBatchSerializer
    http_method_names = ['patch']

    @transaction.atomic
    def partial_update(self, request, *args, **kwargs):
        order_details = request.data.pop('order_details')
        order_details_create = []
        for order_detail in order_details:
            if order_detail.get("id", False):
                order_detail_instance = OrderDetail.objects.get(id=order_detail['id'])

                serializer = UpdateCustomerDetailsByBatchSerializer(
                    order_detail_instance, data=order_detail, partial=True
                )
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                order_details_create.append(order_detail)

        request.data['order_details'] = order_details_create
        return super(UpdateCustomerOrderByBatchAPIView, self).partial_update(request, *args, **kwargs)
