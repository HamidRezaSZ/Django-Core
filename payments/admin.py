from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'status')
    search_fields = ('link', 'status', 'ref_id', 'amount', 'authority')
