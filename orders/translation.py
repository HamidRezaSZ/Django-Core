from modeltranslation.translator import TranslationOptions, translator

from .models import *


class DeliveryTypeTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class OrderStatusTranslationOptions(TranslationOptions):
    fields = ('status',)


translator.register(DeliveryType, DeliveryTypeTranslationOptions)
translator.register(OrderStatus, OrderStatusTranslationOptions)
