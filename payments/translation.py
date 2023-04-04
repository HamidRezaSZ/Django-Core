from modeltranslation.translator import TranslationOptions, translator

from .models import *


class PaymentStatusTranslationOptions(TranslationOptions):
    fields = ('status',)


translator.register(PaymentStatus, PaymentStatusTranslationOptions)
