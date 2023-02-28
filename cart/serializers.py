from rest_framework import serializers

from base.base_serializers import ModelSerializer
from products.serializers import ProductQuantitiesSerializer

from .models import *


class CartItemSerializer(ModelSerializer):
    product_quantity = ProductQuantitiesSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        exclude = ('user',)

    def get_items(self, obj):
        return CartItemSerializer(obj.cartitem_set.all(), many=True).data
