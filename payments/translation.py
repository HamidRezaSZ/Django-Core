from modeltranslation.translator import TranslationOptions, translator

from .models import *


class PaymentStatusTranslationOptions(TranslationOptions):
    fields = ('status',)


class PaymentGateWayTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(PaymentStatus, PaymentStatusTranslationOptions)
translator.register(PaymentGateWay, PaymentGateWayTranslationOptions)
