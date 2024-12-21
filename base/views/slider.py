from rest_framework.permissions import AllowAny, IsAdminUser

from base.models import Slider
from base.serializers.slider import SliderSerializer
from base.views.viewsets import ModelViewSet


class SliderView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Slider.objects.filter(is_active=True).select_related("page")
    serializer_class = SliderSerializer
    filterset_fields = ["page__link", "page"]
