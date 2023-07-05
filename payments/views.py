import json

import requests
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import Response

from base.viewsets import ModelViewSet

from .models import *
from .serializers import *


class PaymentView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = PaymentSerializer
    filterset_fields = ['authority']

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user).select_related('payment_gateway', 'status')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context


class PaymentGateWayView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    serializer_class = PaymentGateWaySerializer

    def get_queryset(self):
        return PaymentGateWay.objects.all()


class VerifyPayment(ListAPIView):

    def get(self, request):
        authority = request.query_params.get('Authority')
        payment_obj = Payment.objects.get(authority=authority)
        data = {
            "MerchantID":  payment_obj.payment_gateway.merchant,
            "Amount": payment_obj.amount,
            "Authority": authority,
        }
        data = json.dumps(data)

        headers = {'content-type': 'application/json',
                   'content-length': str(len(data))}
        response = requests.post(
            payment_obj.payment_gateway.verify_url, data=data, headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                status, created = PaymentStatus.objects.get_or_create(
                    status='موفق')
                payment_obj.status = status
                payment_obj.save(update_fields=['status'])
                return Response({'status': True, 'RefID': response['RefID']})
            else:
                status, created = PaymentStatus.objects.get_or_create(
                    status='ناموفق')
                payment_obj.status = status
                payment_obj.save(update_fields=['status'])
                return Response({'status': False, 'code': str(response['Status'])})

        status, created = PaymentStatus.objects.get_or_create(
            status='لغو شده')
        payment_obj.status = status
        payment_obj.save(update_fields=['status'])
        return Response(response)
