from .serializers import CartSerializer, CartGetSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from base.viewsets import ModelViewSet
from .models import Cart
from django.shortcuts import get_object_or_404


class CartView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_queryset(self):
        return Cart.objects.filter(related_user=self.request.user)

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Cart, pk=pk, related_user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CartGetSerializer
        return CartSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context
