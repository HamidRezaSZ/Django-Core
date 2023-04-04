from modeltranslation.translator import TranslationOptions, translator

from .models import *


class TicketDepartmentTranslationOptions(TranslationOptions):
    fields = ('name',)


class TicketPriorityTranslationOptions(TranslationOptions):
    fields = ('title',)


class TicketStatusTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(TicketDepartment, TicketDepartmentTranslationOptions)
translator.register(TicketPriority, TicketPriorityTranslationOptions)
translator.register(TicketStatus, TicketStatusTranslationOptions)
