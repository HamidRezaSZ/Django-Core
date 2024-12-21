from django.contrib import admin

from base.models import Footer


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    """
    Admin panel for footer
    """

    list_display = ("id",)
    filter_horizontal = ("social_accounts", "useful_link")

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)
