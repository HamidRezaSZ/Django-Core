from django.contrib import admin


class SingletonModelAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        """Singleton pattern: prevent addition of new objects"""
        if self.model.objects.count() == 0:
            return super().has_add_permission(request)
        return False
