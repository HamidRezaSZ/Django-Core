from django.contrib import admin

from base.models import SocialAccount


@admin.register(SocialAccount)
class SocialAccountsAdmin(admin.ModelAdmin):
    list_display = ("id",)
    search_fields = ("link",)
