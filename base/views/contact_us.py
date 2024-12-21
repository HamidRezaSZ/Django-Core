from rest_framework.permissions import AllowAny, IsAdminUser

from base.models import ContactUsDetail, ContactUsForm
from base.serializers.contact_us import (
    ContactUsDetailSerializer,
    ContactUsFormSerializer,
)
from base.views.viewsets import ModelViewSet


class ContactUsFormView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "create": [AllowAny],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = ContactUsFormSerializer
    queryset = ContactUsForm.objects.all()


class ContactUsDetailView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = ContactUsDetail.objects.filter(is_active=True)
    serializer_class = ContactUsDetailSerializer
