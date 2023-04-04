from django.contrib import admin

from .models import *


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'status')
    search_fields = ('link', 'status', 'ref_id', 'amount', 'authority')


@admin.register(PaymentStatus)
class PaymentStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
