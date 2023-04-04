from modeltranslation.translator import TranslationOptions, translator

from .models import *


class QuestionTranslationOptions(TranslationOptions):
    fields = ('question',)


class ChoiceOfMultipleChoiceQuestionTranslationOptions(TranslationOptions):
    fields = ('choice',)


translator.register(Question, QuestionTranslationOptions)
translator.register(ChoiceOfMultipleChoiceQuestion, ChoiceOfMultipleChoiceQuestionTranslationOptions)
