from rest_framework.permissions import AllowAny, IsAdminUser

from base.models import AboutUs
from base.serializers.about_us import AboutUsSerializer
from base.views.viewsets import ModelViewSet


class AboutUsView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = AboutUsSerializer
    queryset = AboutUs.objects.all()
