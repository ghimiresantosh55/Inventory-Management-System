from django.db import transaction
from rest_framework.generics import CreateAPIView

from .serializers import SaveDirectPurchaseMasterSerializer
from ..models import PurchaseMaster


class SaveDirectPurchaseApiView(CreateAPIView):
    queryset = PurchaseMaster.objects.all()
    serializer_class = SaveDirectPurchaseMasterSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super(SaveDirectPurchaseApiView, self).create(request, *args, **kwargs)
