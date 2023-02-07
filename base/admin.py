from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin

admin.site.site_header = "پنل مدیریتی  core"
admin.site.site_title = "پنل مدیریتی  core"


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    search_fields = ('question', 'answer')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
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
class ContactUsDetailAdmin(admin.ModelAdmin):
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
class PageAdmin(admin.ModelAdmin):
    '''
        Admin panel for pages
    '''

    list_display = ('title',)
    search_fields = ('title', 'link')


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    '''
        Admin panel for home page slider
    '''

    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'text', 'link')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'link')


class CityInline(admin.TabularInline):
    model = City
    extra = 0


@admin.register(State)
class StateAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = (CityInline,)
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'state')
    search_fields = ('name',)


@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('id',)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)
