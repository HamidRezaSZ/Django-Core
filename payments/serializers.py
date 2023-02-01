from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ('user',)

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user

        obj = Payment.objects.create(validated_data)

        return obj
