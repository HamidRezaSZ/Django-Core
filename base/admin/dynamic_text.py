from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from base.models import DynamicText


@admin.register(DynamicText)
class DynamicTextAdmin(TranslationAdmin):
    list_display = ("id", "key")
    search_fields = ("key", "value")
