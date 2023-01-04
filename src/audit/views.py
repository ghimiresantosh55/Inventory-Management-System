# Create your views here
from rest_framework.generics import ListAPIView
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet

from .models import Audit
from .serializers import AuditCreateSerializer, AuditReportSerializer
from ..user_group.models import CustomPermission


class AuditCreateApiView(ModelViewSet):
    queryset = Audit.objects.filter(is_finished=False).prefetch_related("audit_details")
    serializer_class = AuditCreateSerializer
    http_method_names = ['post', 'patch']

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, *args, **kwargs)


class AuditReportPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.is_superuser:
            return True

        try:
            groups = request.user.groups.filter(
                is_active=True).values_list('id', flat=True)
            user_permissions = CustomPermission.objects.filter(customgroup__in=groups).values_list(
                'code_name', flat=True
            )
        except Exception:
            return False
        if request.method == 'GET' and 'view_audit_report' in user_permissions:
            return True
        return False


class AuditReportApiView(ListAPIView):
    permission_classes = [AuditReportPermission]
    queryset = Audit.objects.all().prefetch_related("audit_details")
    serializer_class = AuditReportSerializer
