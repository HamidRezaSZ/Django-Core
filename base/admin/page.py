from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from base.models import Page


@admin.register(Page)
class PageAdmin(TranslationAdmin):
    """
    Admin panel for pages
    """

    list_display = (
        "id",
        "title",
    )
    search_fields = ("title", "link")
