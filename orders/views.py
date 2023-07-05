from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from base.viewsets import ModelViewSet

from .models import *
from .serializers import *


class DeliveryTypeViewSet(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = DeliveryTypeSerializer
    queryset = DeliveryType.objects.filter(is_active=True)


class OrderViewSet(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticated],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return OrderGetSerializer

        return OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).select_related('status', 'payment', 'delivery_type', 'address')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context
