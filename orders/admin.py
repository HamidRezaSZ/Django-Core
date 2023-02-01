from django.contrib import admin
from .models import *


@admin.register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'delivery_price')


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product_quantity', 'quantity')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'price', 'status')
    inlines = (OrderItemInline,)
