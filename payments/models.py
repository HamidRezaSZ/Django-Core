from django.db import models
from base.models import BaseModel
from accounts.models import User
from django.conf import settings
import json
import requests


class Payment(models.Model):
    class Status(models.TextChoices):
        SUCCESSFUL = 'S', 'موفق'
        UNSUCCESSFUL = 'U', 'ناموفق'
        CANCELED = 'C', 'لغو شده'
        AWAITONG_PAYMENT = 'A', 'در انتظار پرداخت'

    user = models.ForeignKey(verbose_name='کاربر', to=User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField('مبلغ')
    ref_id = models.CharField('شماره تراکنش', max_length=512, blank=True, null=True)
    status = models.CharField('وضعیت', choices=Status.choices, max_length=20, default='در انتظار پرداخت')
    authority = models.CharField('شناسه مرجع', max_length=512, blank=True, null=True)
    link = models.URLField('لینک درگاه پرداخت', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    def __str__(self):
        return f'{self.user} - {self.amount} : {self.status}'

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت ها'
        ordering = ('created_date',)

    def save(self, *args, **kwargs):
        if not self.pk:
            description = 'D-Pay'
            req_data = {
                "merchant_id": settings.MERCHANT,
                "amount": self.amount,
                "callback_url": settings.CALLBACKURL,
                "description": description
            }
            req_header = {"accept": "application/json",
                          "content-type": "application/json'"}
            req = requests.post(url=settings.ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
            authority = req.json()['data']['authority']

            if len(req.json()['errors']) == 0:
                self.authority = authority
                self.link = settings.ZP_API_STARTPAY.format(authority=authority)
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                self.error = f"Error code: {e_code}, Error Message: {e_message}"

        super(Payment, self).save(*args, **kwargs)
