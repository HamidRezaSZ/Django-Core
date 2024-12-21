from django.contrib import admin

from base.models import ObjectInstance


@admin.register(ObjectInstance)
class ObjectInstanceAdmin(admin.ModelAdmin):
    pass
