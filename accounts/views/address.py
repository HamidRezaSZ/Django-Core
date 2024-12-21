from rest_framework.permissions import IsAuthenticated

from accounts.models import Address
from accounts.serializers.address import AddressGetSerializer, AddressSerializer
from base.views.viewsets import ModelViewSet


class AddressesView(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return AddressGetSerializer

        return AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user).select_related("city")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context
