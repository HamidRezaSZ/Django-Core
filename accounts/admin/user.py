from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from accounts.models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("email", "cell_phone", "avatar", "gender", "national_id")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    list_display = ("id", "username", "email", "cell_phone", "is_staff", "is_active")
    list_editable = ("is_staff", "is_active")
    search_fields = ("national_id", "username", "first_name", "last_name", "email")
    ordering = ("username",)
