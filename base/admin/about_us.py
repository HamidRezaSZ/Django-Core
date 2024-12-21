from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from base.models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    list_display = ("id",)
    search_fields = ("text",)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)
