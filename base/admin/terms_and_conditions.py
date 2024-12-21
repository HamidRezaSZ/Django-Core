from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from base.models import TermsAndConditions


@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(TranslationAdmin):
    list_display = ("id",)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)