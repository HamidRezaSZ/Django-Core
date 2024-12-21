from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from base.models import ContactUsDetail, ContactUsForm


@admin.register(ContactUsForm)
class ContactUsFormAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "cell_phone_number")
    search_fields = ("message",)
    readonly_fields = ("full_name", "cell_phone_number", "message")


@admin.register(ContactUsDetail)
class ContactUsDetailAdmin(TranslationAdmin):
    list_display = ("id",)
    filter_horizontal = ("social_accounts",)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)
