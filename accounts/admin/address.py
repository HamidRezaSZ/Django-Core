from django.contrib import admin

from accounts.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    search_fields = ("address", "zip_code", "description")
