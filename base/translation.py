from modeltranslation.translator import TranslationOptions, translator

from .models import *


class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('text',)


class ContactUsDetailTranslationOptions(TranslationOptions):
    fields = ('email', 'phone_number')


class PageTranslationOptions(TranslationOptions):
    fields = ('title',)


class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


class FooterTranslationOptions(TranslationOptions):
    fields = ('content',)


class StateTranslationOptions(TranslationOptions):
    fields = ('name',)


class CityTranslationOptions(TranslationOptions):
    fields = ('name',)


class TermsAndConditionsTranslationOptions(TranslationOptions):
    fields = ('text',)


translator.register(FAQ, FAQTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(ContactUsDetail, ContactUsDetailTranslationOptions)
translator.register(Page, PageTranslationOptions)
translator.register(Slider, SliderTranslationOptions)
translator.register(Footer, FooterTranslationOptions)
translator.register(State, StateTranslationOptions)
translator.register(City, CityTranslationOptions)
translator.register(TermsAndConditions, TermsAndConditionsTranslationOptions)
