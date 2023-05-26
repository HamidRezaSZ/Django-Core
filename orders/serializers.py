from rest_framework import serializers

from accounts.serializers import AddressSerializer
from base.base_serializers import ModelSerializer
from payments.serializers import PaymentSerializer
from products.models import Coupon
from products.serializers import ProductQuantitiesSerializer

from .models import *


class DeliveryTypeSerializer(ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    product_quantity = ProductQuantitiesSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderStatusSerializer(ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderGetSerializer(ModelSerializer):
    address = AddressSerializer()
    payment = PaymentSerializer()
    delivery_type = DeliveryTypeSerializer()
    items = serializers.SerializerMethodField()
    status = OrderStatusSerializer()

    class Meta:
        model = Order
        exclude = ('user',)
        read_only_fields = ('status', 'discount_amount', 'price', 'payment')

    def get_items(self, obj):
        return OrderItemSerializer(obj.orderitem_set.all(), many=True).data


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        exclude = ('user',)
        read_only_fields = ('price', 'payment', 'status', 'discount_amount')

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user

        coupon = validated_data['coupon']
        if coupon:
            coupon_exist = Coupon.objects.filter(discount_code=coupon)
            if coupon_exist.exists():
                coupon_obj = coupon_exist.first()
                if coupon_obj.user and not coupon_obj.check_user(user):
                    raise serializers.ValidationError('This code is not for this user!')
                else:
                    if coupon_obj.user and coupon_obj.discount_amount != 0:
                        validated_data['discount_amount'] = coupon_obj.discount_amount
                    elif coupon_obj.user and coupon_obj.discount_percent != 0:
                        cart_obj = Cart.objects.get_or_create(user=user)
                        price = cart_obj.get_cart_price()
                        validated_data['discount_amount'] = price * (coupon_obj.discount_percent/100)
            else:
                raise serializers.ValidationError('Coupon code is wrong!')

        return super().create(validated_data)
