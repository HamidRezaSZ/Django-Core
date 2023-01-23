from django.contrib import admin
from .models import NewsLetters
from import_export.admin import ExportActionMixin


@admin.register(NewsLetters)
class NewsLettersAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
