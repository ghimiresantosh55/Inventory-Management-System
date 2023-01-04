from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import serializers

from src.custom_lib.functions import current_user
from src.item_serialization.models import PackingTypeDetailCode
from .audit_no_generator import generate_audit_no
from .audit_service import generate_audit
from .models import Audit, AuditDetail


class AuditDetailCreateSerializer(serializers.ModelSerializer):
    packing_type_detail_code = serializers.CharField(max_length=50)

    class Meta:
        model = AuditDetail
        fields = ['packing_type_detail_code']


class AuditCreateSerializer(serializers.ModelSerializer):
    audit_details = AuditDetailCreateSerializer(many=True)

    class Meta:
        model = Audit
        fields = ['id', 'audit_no', 'audit_details', 'remarks', 'is_finished']
        read_only_fields = ['audit_no']
        # extra_kwargs = {
        #     'packing_type_detail_code_nos': {'write_only': True}
        # }

    def create(self, validated_data):
        date_now = timezone.now()
        created_by_user = current_user.get_created_by(self.context)
        audit_details = validated_data.pop('audit_details')
        audit = Audit.objects.create(
            **validated_data,
            audit_no=generate_audit_no(),
            created_date_ad=date_now,
            created_by=created_by_user
        )

        for audit_detail in audit_details:
            try:
                pack_type_detail_code = PackingTypeDetailCode.objects.filter(
                    ref_packing_type_detail_code__isnull=True).get(code=audit_detail['packing_type_detail_code'])
            except ObjectDoesNotExist:
                raise serializers.ValidationError(
                    {"message": f"this : {audit_detail['packing_type_detail_code']} does not exist"})
            AuditDetail.objects.create(
                audit=audit,
                detail_type=2,
                packing_type_detail_code=pack_type_detail_code,
                created_by=audit.created_by,
                created_date_ad=audit.created_date_ad
            )

        if audit.is_finished:
            generate_audit(audit)
        return audit

    def update(self, instance, validated_data):

        audit_details = validated_data.pop('audit_details')
        instance.is_finished = validated_data.get("is_finished", instance.is_finished)
        instance.remarks = validated_data.get("remarks", instance.remarks)

        for audit_detail in audit_details:
            try:
                pack_type_detail_code = PackingTypeDetailCode.objects.get(code=audit_detail['packing_type_detail_code'])
            except ObjectDoesNotExist:
                raise serializers.ValidationError(
                    {"message": f"this : {audit_detail['packing_type_detail_code']} does not exist"})
            AuditDetail.objects.create(
                audit=instance,
                detail_type=2,
                packing_type_detail_code=pack_type_detail_code,
                created_by=instance.created_by,
                created_date_ad=instance.created_date_ad
            )

        if instance.is_finished:
            generate_audit(instance)
        return instance


class AuditReportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditDetail
        fields = ['id', 'detail_type', 'packing_type_detail_code']


class AuditReportSerializer(serializers.ModelSerializer):
    audit_details = AuditReportDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Audit
        fields = ['id', 'audit_no', 'remarks', 'is_finished', 'audit_details']
        read_only_fields = fields
