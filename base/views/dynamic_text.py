from rest_framework.permissions import AllowAny, IsAdminUser

from base.models import DynamicText
from base.serializers.dynamic_text import DynamicTextSerializer
from base.views.viewsets import ModelViewSet


class DynamicTextView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = DynamicTextSerializer
    queryset = DynamicText.objects.filter(is_active=True)
    filterset_fields = ["key"]
