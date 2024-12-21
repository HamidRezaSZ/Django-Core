from django.contrib import admin

from base.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "page", "parent", "order")
    list_editable = ("order",)
    search_fields = ("page",)
