import json

import requests
from django.conf import settings
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
        return Payment.objects.filter(user=self.request.user)

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Payment, pk=pk, user=self.request.user)


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

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(PaymentGateWay, pk=pk)


class VerifyPayment(ListAPIView):

    def get(self, request, authority, status):
        payment_obj = Payment.objects.get(authority=authority)

        if status == 'OK':
            req_header = {"accept": "application/json",
                          "content-type": "application/json'"}
            req_data = {
                "merchant_id": settings.MERCHANT,
                "amount": payment_obj.amount,
                "authority": authority
            }
            req = requests.post(url=settings.ZP_API_VERIFY,
                                data=json.dumps(req_data), headers=req_header)
            if len(req.json()['errors']) == 0:
                t_status = req.json()['data']['code']
                if t_status == 100:
                    payment_obj.status = 'موفق'
                    payment_obj.save(update_fields=['status'])

                    return Response('Transaction success.\nRefID: ' + str(
                        req.json()['data']['ref_id']
                    ))
                elif t_status == 101:
                    return Response('Transaction submitted : ' + str(
                        req.json()['data']['message']
                    ))
                else:
                    payment_obj.status = 'ناموفق'
                    payment_obj.save(update_fields=['status'])

                    return Response('Transaction failed.\nStatus: ' + str(
                        req.json()['data']['message']
                    ))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return Response(f"Error code: {e_code}, Error Message: {e_message}")
        else:
            payment_obj.status = 'لغو شده'
            payment_obj.save(update_fields=['status'])

            return Response('Transaction failed or canceled by user')
