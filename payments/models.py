import json

import requests
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from base.models import BaseModel


class PaymentStatus(BaseModel):
    status = models.CharField(max_length=200, verbose_name=_('status'))

    class Meta:
        verbose_name = _('Payment Status')
        verbose_name_plural = _('Payment Statuses')

    def __str__(self) -> str:
        return self.status


class PaymentGateWay(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    icon = models.FileField(upload_to='payment-icons', verbose_name=_('icon'))
    request_url = models.CharField(
        max_length=500, verbose_name=_('request_url'))
    verify_url = models.CharField(max_length=500, verbose_name=_('verify_url'))
    startpay_url = models.CharField(
        max_length=500, verbose_name=_('startpay_url'))
    merchant = models.CharField(max_length=200, verbose_name=_('merchant'))

    class Meta:
        verbose_name = _('Payment GateWay')
        verbose_name_plural = _('Payment GateWays')

    def __str__(self) -> str:
        return self.title


class Payment(models.Model):
    user = models.ForeignKey(verbose_name=_(
        'user'), to=User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name=_('amount'))
    ref_id = models.CharField(verbose_name=_(
        'ref_id'), max_length=512, blank=True, null=True)
    status = models.ForeignKey(
        to=PaymentStatus, on_delete=models.CASCADE, verbose_name=_('status'))
    authority = models.CharField(verbose_name=_(
        'authority'), max_length=512, blank=True, null=True)
    link = models.URLField(verbose_name=_('link'), blank=True, null=True)
    payment_gateway = models.ForeignKey(to=PaymentGateWay, verbose_name=_(
        'payment_gateway'), on_delete=models.PROTECT)
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created_date'))

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
        ordering = ('created_date',)

    def __str__(self) -> str:
        return f'{self.user} - {self.amount} : {self.status}'

    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            data = {
                "MerchantID": self.payment_gateway.merchant,
                "Amount": self.amount,
                "Description": "Core",
                "CallbackURL": settings.CALLBACKURL,
            }
            data = json.dumps(data)
            headers = {'content-type': 'application/json', 'content-length': str(len(data))}
            status, created = PaymentStatus.objects.get_or_create(
                status='Pending')
            self.status = status
            try:
                response = requests.post(self.payment_gateway.request_url, data=data, headers=headers, timeout=10)
                if response.status_code == 200:
                    response = response.json()
                    if response['Status'] == 100:
                        self.authority = response['Authority']
                        self.link = self.payment_gateway.startpay_url + str(response['Authority'])
                        self.status = status
                    else:
                        status, created = PaymentStatus.objects.get_or_create(
                            status=response['Status'])
                        self.status = status

                status, created = PaymentStatus.objects.get_or_create(
                    status='Error')
                self.status = status
            except Exception:
                status, created = PaymentStatus.objects.get_or_create(
                    status='Error')
                self.status = status

        super(Payment, self).save(*args, **kwargs)
