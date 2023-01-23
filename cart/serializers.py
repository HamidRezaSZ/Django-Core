from rest_framework import serializers
from .models import Cart
from orders.serializers import OrderProductQuantitySerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ('related_user',)

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['related_user'] = user

        return super().create(validated_data)

    def validate_related_order_product_quantity(self, value):
        for item in value.all():
            if item.related_product_quantity.quantity < item.quantity:
                raise serializers.ValidationError('The item is unavailable')
        return value


class CartGetSerializer(serializers.ModelSerializer):
    related_order_product_quantity = OrderProductQuantitySerializer(many=True)

    class Meta:
        model = Cart
        exclude = ('related_user',)
