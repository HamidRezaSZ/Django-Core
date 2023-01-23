from django.contrib import admin
from .models import *


@admin.register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'delivery_price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_user', 'related_delivery_type', 'status')
    filter_horizontal = ('related_order_product_quantity',)
