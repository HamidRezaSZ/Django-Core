from rest_framework.permissions import AllowAny, IsAdminUser

from base.models import Footer
from base.serializers.footer import FooterSerializer
from base.views.viewsets import ModelViewSet


class FooterView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Footer.objects.filter(is_active=True).select_related("contact_us")
    serializer_class = FooterSerializer
