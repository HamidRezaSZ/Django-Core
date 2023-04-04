from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportMixin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import *

admin.site.site_header = _('Core Admin Panel')
admin.site.site_title = _('Core Admin Panel')


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('id', 'question')
    search_fields = ('question', 'answer')


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    list_display = ('id',)
    search_fields = ('text',)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)


@admin.register(ContactUsForm)
class ContactUsFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'cell_phone_number')
    search_fields = ('message',)
    readonly_fields = ('full_name', 'cell_phone_number', 'message')


@admin.register(SocialAccount)
class SocialAccountsAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('link',)


@admin.register(ContactUsDetail)
class ContactUsDetailAdmin(TranslationAdmin):
    list_display = ('id',)
    filter_horizontal = ('social_accounts',)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    '''
        Admin panel for footer
    '''

    list_display = ('id',)
    filter_horizontal = ('social_accounts', 'useful_link')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)


@admin.register(Page)
class PageAdmin(TranslationAdmin):
    '''
        Admin panel for pages
    '''

    list_display = ('id', 'title',)
    search_fields = ('title', 'link')


@admin.register(Slider)
class SliderAdmin(TranslationAdmin):
    '''
        Admin panel for home page slider
    '''

    list_display = ('id', 'title', 'page', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'text', 'link')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'page', 'parent', 'order')
    list_editable = ('order',)
    search_fields = ('page',)


class CityInline(TranslationTabularInline):
    model = City
    extra = 0


@admin.register(State)
class StateAdmin(ImportExportMixin, TranslationAdmin):
    list_display = ('id', 'name')
    inlines = (CityInline,)
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(ImportExportMixin, TranslationAdmin):
    list_display = ('id', 'name', 'state')
    search_fields = ('name',)


@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(TranslationAdmin):
    list_display = ('id',)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)


class ComponentItemInline(admin.TabularInline):
    model = ComponentItem
    extra = 0


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'page', 'parent')
    inlines = (ComponentItemInline,)
