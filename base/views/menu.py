from rest_framework.permissions import AllowAny, IsAdminUser

from base.models import Menu
from base.serializers.menu import MenuSerializer
from base.views.viewsets import ModelViewSet


class MenuView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Menu.objects.filter(is_active=True, parent=None).select_related("page")
    serializer_class = MenuSerializer
