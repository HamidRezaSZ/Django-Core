from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_user')
    filter_horizontal = ('related_order_product_quantity',)
