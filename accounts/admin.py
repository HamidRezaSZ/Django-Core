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
             ('email', 'cell_phone', 'avatar', 'gender', 'national_id', 'related_city')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),)

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    list_display = ('id', 'username', 'email', 'cell_phone', 'is_staff', 'is_active')
    list_editable = ('is_staff', 'is_active')
    ordering = ('username',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_user')




@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_user')
