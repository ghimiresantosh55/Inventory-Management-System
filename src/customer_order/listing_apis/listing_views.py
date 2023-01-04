from decimal import Decimal

import django_filters
from django.db import connection
from django.db.models import OuterRef, Subquery, Sum, Count, DecimalField, Q, Max
from django.db.models.functions import Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from src.core_app.models import DiscountScheme
from src.customer.models import Customer
from src.item.models import Item
from src.purchase.models import PurchaseDetail
from tenant.models import Tenant
from .listing_serializers import (CustomerCustomerOrderListSerializer,
                                  DiscountSchemeCustomerOrderListSerializer, ItemCustomerOrderListSerializer,
                                  SelfCustomerOrderListSerializer, TransferBranchListSerializer)
from ..models import OrderMaster
from tenant.utils import tenant_schema_from_request


class CustomerListApiView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCustomerOrderListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'middle_name', 'last_name', 'pan_vat_no']
    ordering_fields = ['id', 'first_name']


class DiscountSchemeListApiView(ListAPIView):
    queryset = DiscountScheme.objects.all()
    serializer_class = DiscountSchemeCustomerOrderListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']


class ItemListFilterForCustomerOrder(django_filters.FilterSet):
    id = django_filters.ModelMultipleChoiceFilter(queryset=Item.objects.filter(active=True),
                                                  to_field_name='id')

    class Meta:
        model = Item
        fields = ['id', 'name']


class ItemListApiView(ListAPIView):
    serializer_class = ItemCustomerOrderListSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filter_class = ItemListFilterForCustomerOrder
    search_fields = ['name']
    ordering_fields = ['id', 'name']

    def get_queryset(self):
        transfer_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
            transfer_qty=Sum('transferdetail__qty', filter=Q(transferdetail__transfer_master__transfer_type=1,
                                                             transferdetail__cancelled=False))
        ).values("transfer_qty")
        transfer_return_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
            transfer_return_qty=Sum('transferdetail__qty', filter=Q(transferdetail__transfer_master__transfer_type=2,
                                                                    transferdetail__cancelled=False))
        ).values("transfer_return_qty")
        asset_count = Item.objects.filter(pk=OuterRef("pk")).annotate(
            asset_count=Count(
                'purchasedetail__pu_pack_type_codes__pack_type_detail_codes__assetlist',
                filter=Q(purchasedetail__ref_purchase_detail__isnull=True)
            )
        ).values('asset_count')
        purchase_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
            purchase_qty=Sum(
                'purchasedetail__qty',
                filter=Q(purchasedetail__purchase__purchase_type__in=[1, 3, 4])
                # & Q(purchasedetail__pu_pack_type_codes__location__isnull=False)
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
                filter=Q(saledetail__sale_master__sale_type=2, saledetail__sale_master__return_dropped=True)
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
                filter=Q(chalandetail__chalan_master__status=3, chalandetail__chalan_master__return_dropped=True)
            )
        ).values('chalan_return_qty')

        pending_customer_order_qty = Item.objects.filter(pk=OuterRef("pk")).annotate(
            pending_customer_order_qty=Sum(
                'orderdetail__qty',
                filter=Q(orderdetail__cancelled=False, orderdetail__order__status=1)
            )
        ).values('pending_customer_order_qty')

        highest_sale_cost = PurchaseDetail.objects.filter(item=OuterRef("id")).values('item').annotate(
            highest_sale_cost=Max("sale_cost")
        ).values("highest_sale_cost")

        queryset = Item.objects.filter(active=True).annotate(
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
            ),
            item_highest_cost=Subquery(highest_sale_cost, output_field=DecimalField())
        ).values(
            'id', 'purchase_cost', 'item_highest_cost', 'name', 'discountable',
            'taxable', 'tax_rate', 'code', 'item_category',
            'remaining_qty', 'sale_cost'
        ).filter(remaining_qty__gt=0)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(queryset, status=status.HTTP_200_OK)


class SelfCustomerOrderListAPIView(ListAPIView):
    serializer_class = SelfCustomerOrderListSerializer
    pagination_class = None

    def get_queryset(self):
        if self.request.user:
            return OrderMaster.objects.filter(created_by=self.request.user).order_by('-created_date_ad')[:5]
        return OrderMaster.objects.none()

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset().order_by('-id')
    #
    #     page = queryset[:5]
    #     return Response(page, status=status.HTTP_200_OK)


class TransferBranchListAPIView(ListAPIView):
    serializer_class = TransferBranchListSerializer
    permission_classes = [AllowAny]
    queryset = Tenant.objects.all()

    def list(self, request, *args, **kwargs):
        connection.cursor().execute(f"SET search_path to public")

        queryset = self.filter_queryset(Tenant.objects.exclude(schema_name=tenant_schema_from_request(request)))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = TransferBranchListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
