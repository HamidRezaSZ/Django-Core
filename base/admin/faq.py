from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from base.models import FAQ


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ("id", "question")
    search_fields = ("question", "answer")
