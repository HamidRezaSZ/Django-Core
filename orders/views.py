from base.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404


class DeliveryTypeViewSet(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = DeliveryTypeSerializer
    queryset = DeliveryType.objects.filter(is_active=True)


class OrderProductQuantityViewSet(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "post": [IsAuthenticated],
        "update": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAdminUser],
    }

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return OrderProductQuantityGetSerializer

        return OrderProductQuantitySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context

    def get_queryset(self):
        return OrderProductQuantity.objects.filter(is_active=True, related_user=self.request.user)

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(OrderProductQuantity, pk=pk, related_user=self.request.user)


class OrderViewSet(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "post": [IsAuthenticated],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return OrderItemSerializer

        return OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(is_active=True, related_user=self.request.user)

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Order, pk=pk, related_user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context
