from modeltranslation.translator import TranslationOptions, translator

from .models import *


class QuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'choice_one', 'choice_two',
              'choice_three', 'choice_four')


class ExamTranslationOptions(TranslationOptions):
    fields = ('title',)


class DescriptiveAnswerTranslationOptions(TranslationOptions):
    fields = ('content',)


translator.register(Question, QuestionTranslationOptions)
translator.register(Exam, ExamTranslationOptions)
translator.register(DescriptiveAnswer, DescriptiveAnswerTranslationOptions)
