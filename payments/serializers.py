from base.serializers.base_serializers import ModelSerializer

from .models import *


class PaymentStatusSerializer(ModelSerializer):

    class Meta:
        model = PaymentStatus
        fields = '__all__'


class PaymentGateWaySerializer(ModelSerializer):

    class Meta:
        model = PaymentGateWay
        fields = ('id', 'title', 'icon')


class PaymentSerializer(ModelSerializer):
    status = PaymentStatusSerializer()

    class Meta:
        model = Payment
        exclude = ('user',)

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user

        obj = Payment.objects.create(validated_data)

        return obj
