from django.contrib import admin

from base.admin.singleton import SingletonModelAdmin
from base.models import Footer, FooterColumn, FooterImage, FooterRow


class FooterRowInline(admin.TabularInline):
    model = FooterRow
    extra = 0


@admin.register(Footer)
class FooterAdmin(SingletonModelAdmin):
    list_display = ("id", "text", "logo")


@admin.register(FooterColumn)
class FooterColumnAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "link", "order")
    list_editable = ("order",)
    search_fields = ("title", "link")
    inlines = (FooterRowInline,)


@admin.register(FooterImage)
class FooterImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "link", "order")
    list_editable = ("order",)
    search_fields = ("link",)
