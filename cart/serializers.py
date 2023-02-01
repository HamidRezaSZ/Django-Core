from rest_framework import serializers
from .models import *
from products.serializers import ProductQuantitiesSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product_quantity = ProductQuantitiesSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        exclude = ('user',)

    def get_items(self, obj):
        return CartItemSerializer(obj.cartitem_set.all(), many=True).data
