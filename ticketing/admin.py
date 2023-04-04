from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


class TicketMessageInline(admin.TabularInline):
    model = TicketMessage
    extra = 0


class MessageFileInline(admin.TabularInline):
    model = MessageFile
    extra = 0


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'priority', 'subject', 'created_date', 'status', 'is_archive')
    list_editable = ('is_archive',)
    search_fields = ('subject',)
    inlines = (TicketMessageInline,)


@admin.register(TicketDepartment)
class DepartmentAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('name',)


@admin.register(TicketPriority)
class PriorityAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title',)


@admin.register(TicketStatus)
class StatusAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title',)


@admin.register(MessageFile)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')


class MessageFileInline(admin.TabularInline):
    model = MessageFile


@admin.register(TicketMessage)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    inlines = (MessageFileInline,)
    search_fields = ('content',)
