from rest_framework.permissions import AllowAny, IsAdminUser

from base.models import FAQ
from base.serializers.faq import FAQSerializer
from base.views.viewsets import ModelViewSet


class FAQView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    serializer_class = FAQSerializer
    queryset = FAQ.objects.filter(is_active=True)
