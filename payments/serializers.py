from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ('related_user',)

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['related_user'] = user

        obj = Payment.objects.create(validated_data)

        return obj
