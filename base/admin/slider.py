from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from base.models import Slider


@admin.register(Slider)
class SliderAdmin(TranslationAdmin):
    """
    Admin panel for home page slider
    """

    list_display = ("id", "title", "page", "order")
    list_editable = ("order",)
    search_fields = ("title", "text", "link")
