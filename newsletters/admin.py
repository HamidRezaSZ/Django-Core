from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import NewsLetters


@admin.register(NewsLetters)
class NewsLettersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
