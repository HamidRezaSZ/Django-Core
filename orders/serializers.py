from rest_framework import serializers
from .models import *
from accounts.serializers import AddressSerializer
from payments.serializers import PaymentSerializer
from products.models import Coupon
from products.serializers import ProductSerializer


class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = '__all__'


class OrderProductQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProductQuantity
        exclude = ('related_user',)

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['related_user'] = user

        cart_obj = Cart.objects.get(related_user=user)
        order_quantity_obj = cart_obj.related_order_product_quantity.filter(
            related_product=validated_data['related_product'])
        if order_quantity_obj.exists():
            order_quantity_obj.first().quantity += validated_data.get('quantity') or 1
            order_quantity_obj.first().save()
            return order_quantity_obj.first()

        return super().create(validated_data)


class OrderProductQuantityGetSerializer(serializers.ModelSerializer):
    related_product_quantity = ProductSerializer()

    class Meta:
        model = OrderProductQuantity
        exclude = ('related_user',)


class OrderItemSerializer(serializers.ModelSerializer):
    related_order_product_quantity = OrderProductQuantitySerializer(many=True)
    related_address = AddressSerializer()
    payment = PaymentSerializer()
    related_delivery_type = DeliveryTypeSerializer()

    class Meta:
        model = Order
        exclude = ('related_user',)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('related_user',)
        read_only_fields = ('price', 'payment', 'status', 'related_order_product_quantity')

    def validate_related_order_product_quantity(self, value):
        for item in value.all():
            if item.related_product_quantity.quantity < item.quantity:
                raise serializers.ValidationError('The item is unavailable')
        return value

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['related_user'] = user
        cart_obj = Cart.objects.get(related_user=user)
        price = sum([obj.get_price() for obj in cart_obj.related_order_product_quantity.all()])
        validated_data['price'] = price

        coupon = validated_data['coupon']
        if coupon:
            coupon_exist = Coupon.objects.filter(discount_code=coupon)
            if coupon_exist.exists():
                coupon_obj = coupon_exist.first()
                if coupon_obj.related_user and not coupon_obj.check_user(user):
                    raise serializers.ValidationError('This code is not for this user!')
                else:
                    if coupon_obj.related_user and coupon_obj.discount_amount != 0:
                        validated_data['discount_amount'] = coupon_obj.discount_amount
                    elif coupon_obj.related_user and coupon_obj.discount_percent != 0:
                        validated_data['discount_amount'] = price * (coupon_obj.discount_percent/100)

            else:
                raise serializers.ValidationError('Coupon code is wrong!')

        validated_data['descounted_price'] = price - validated_data['discount_amount']

        return super().create(validated_data)
