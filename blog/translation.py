from modeltranslation.translator import TranslationOptions, translator

from .models import *


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class AuthorTranslationOptions(TranslationOptions):
    fields = ('about',)


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content')


class TagTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Author, AuthorTranslationOptions)
translator.register(Post, PostTranslationOptions)
translator.register(Tag, TagTranslationOptions)
