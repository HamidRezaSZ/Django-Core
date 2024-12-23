from modeltranslation.translator import TranslationOptions, translator

from base.models import (
    FAQ,
    AboutUs,
    City,
    ContactUsDetail,
    DynamicText,
    Footer,
    Page,
    Slider,
    State,
    TermsAndConditions,
)
from base.models.footer import FooterColumn, FooterImage, FooterRow


class FAQTranslationOptions(TranslationOptions):
    fields = ("question", "answer")


class AboutUsTranslationOptions(TranslationOptions):
    fields = ("text",)


class ContactUsDetailTranslationOptions(TranslationOptions):
    fields = ("email", "phone_number")


class PageTranslationOptions(TranslationOptions):
    fields = ("title",)


class SliderTranslationOptions(TranslationOptions):
    fields = ("title", "text")


class FooterTranslationOptions(TranslationOptions):
    fields = ("text",)


class FooterRowTranslationOptions(TranslationOptions):
    fields = ("link", "title")


class FooterColumnTranslationOptions(TranslationOptions):
    fields = ("link", "title")


class FooterImageTranslationOptions(TranslationOptions):
    fields = ("link",)


class StateTranslationOptions(TranslationOptions):
    fields = ("name",)


class CityTranslationOptions(TranslationOptions):
    fields = ("name",)


class TermsAndConditionsTranslationOptions(TranslationOptions):
    fields = ("text",)


class DynamicTextTranslationOptions(TranslationOptions):
    fields = ("value",)


translator.register(FAQ, FAQTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(ContactUsDetail, ContactUsDetailTranslationOptions)
translator.register(Page, PageTranslationOptions)
translator.register(Slider, SliderTranslationOptions)
translator.register(Footer, FooterTranslationOptions)
translator.register(FooterRow, FooterRowTranslationOptions)
translator.register(FooterImage, FooterImageTranslationOptions)
translator.register(FooterColumn, FooterColumnTranslationOptions)
translator.register(State, StateTranslationOptions)
translator.register(City, CityTranslationOptions)
translator.register(TermsAndConditions, TermsAndConditionsTranslationOptions)
translator.register(DynamicText, DynamicTextTranslationOptions)
