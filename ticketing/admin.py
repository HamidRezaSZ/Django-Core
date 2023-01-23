from django.contrib import admin
from .models import *


class TicketDepartmentInline(admin.TabularInline):
    model = TicketDepartment.ticket.through
    verbose_name = 'دپارتمان'
    verbose_name_plural = 'دپارتمان ها'
    extra = 1
    max_num = 1


class TicketPriorityInline(admin.TabularInline):
    model = TicketPriority.ticket.through
    verbose_name = 'اولویت'
    verbose_name_plural = 'اولویت ها'
    extra = 1
    max_num = 1


class TicketStatusInline(admin.TabularInline):
    model = TicketStatus.ticket.through
    verbose_name = 'وضعیت'
    verbose_name_plural = 'وضعیت ها'
    extra = 1
    max_num = 1


class TicketMessageInline(admin.TabularInline):
    model = TicketMessage
    verbose_name = 'پیام'
    verbose_name_plural = 'پیام ها'
    filter_vertical = ('message',)
    extra = 1
    max_num = 1


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'created_date', 'is_archive')
    list_editable = ('is_archive',)
    inlines = (TicketDepartmentInline, TicketPriorityInline, TicketStatusInline, TicketMessageInline)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_editable = ('is_active',)


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    list_editable = ('is_active',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    list_editable = ('is_active',)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')


class MessageFileInline(admin.TabularInline):
    model = MessageFile
    verbose_name = 'فایل'
    verbose_name_plural = 'فایل ها'
    extra = 1
    max_num = 1


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    inlines = (MessageFileInline,)
