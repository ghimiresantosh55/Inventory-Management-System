from django.urls import path
from rest_framework import routers
from .views import AuditCreateApiView, AuditReportApiView

router = routers.DefaultRouter(trailing_slash=False)
router.register("save-audit", AuditCreateApiView)

urlpatterns = [

    # path('save-audit', AuditCreateApiView.as_view({'post': 'create'})),
    # path('save-audit/<int:id>', AuditCreateApiView.as_view({'patch': 'partial_update'})),
    path('audit-report', AuditReportApiView.as_view())
] + router.urls
