from rest_framework.permissions import AllowAny, IsAdminUser

from base.models import City, State
from base.serializers.state import CitySerializer, StateItemSerializer, StateSerializer
from base.views.viewsets import ModelViewSet


class CityView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = City.objects.filter(is_active=True).select_related("state")
    serializer_class = CitySerializer
    filterset_fields = ["state"]


class StateView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = State.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return StateItemSerializer

        return StateSerializer
