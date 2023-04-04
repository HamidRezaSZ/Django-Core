from modeltranslation.translator import TranslationOptions, translator

from .models import *


class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ProductBrandTranslationOptions(TranslationOptions):
    fields = ('title',)


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'description')


class ProductAttributeTranslationOptions(TranslationOptions):
    fields = ('title',)


class ProductAttributeValueTranslationOptions(TranslationOptions):
    fields = ('value',)


class ProductTagTranslationOptions(TranslationOptions):
    fields = ('tag',)


translator.register(ProductCategory, ProductCategoryTranslationOptions)
translator.register(ProductBrand, ProductBrandTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(ProductAttribute, ProductAttributeTranslationOptions)
translator.register(ProductAttributeValue, ProductAttributeValueTranslationOptions)
translator.register(ProductTag, ProductTagTranslationOptions)
