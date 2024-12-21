from django.contrib import admin
from import_export.admin import ImportExportMixin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from base.models import City, State


class CityInline(TranslationTabularInline):
    model = City
    extra = 0


@admin.register(State)
class StateAdmin(ImportExportMixin, TranslationAdmin):
    list_display = ("id", "name")
    inlines = (CityInline,)
    search_fields = ("name",)


@admin.register(City)
class CityAdmin(ImportExportMixin, TranslationAdmin):
    list_display = ("id", "name", "state")
    search_fields = ("name",)
