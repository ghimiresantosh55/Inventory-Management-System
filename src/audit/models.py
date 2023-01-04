from django.db import models

from src.core_app.models import CreateInfoModel
from src.item_serialization.models import PackingTypeDetailCode


# Create your models here.


class Audit(CreateInfoModel):
    audit_no = models.CharField(max_length=20, unique=True, help_text="Audit no. should be max. of 10 characters")
    remarks = models.CharField(max_length=100, blank=True, help_text="Remarks should be max. of 100 characters")
    is_finished = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}: {self.audit_no}"


class AuditDetail(CreateInfoModel):
    DETAIL_TYPES = [
        (1, "AVAILABLE"),
        (2, "AUDITED"),
        (3, "MISSING")
    ]

    audit = models.ForeignKey(Audit, related_name='audit_details', on_delete=models.PROTECT)
    detail_type = models.IntegerField(choices=DETAIL_TYPES)
    packing_type_detail_code = models.ForeignKey(PackingTypeDetailCode, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id} : {self.packing_type_detail_code} : {self.detail_type}"
