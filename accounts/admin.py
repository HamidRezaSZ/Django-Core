from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import *


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    """
    Custom UserAdmin
    """

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
         {
             'fields':
             ('email', 'cell_phone', 'avatar', 'gender', 'national_id', 'city')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),)

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    list_display = ('id', 'username', 'email', 'cell_phone', 'is_staff', 'is_active')
    list_editable = ('is_staff', 'is_active')
    search_fields = ('national_id', 'username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('address', 'zip_code', 'description')
