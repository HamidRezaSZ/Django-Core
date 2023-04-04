from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import *


class ChoiceOfMultipleChoiceQuestionInline(TranslationTabularInline):
    model = ChoiceOfMultipleChoiceQuestion
    extra = 0
    fields = ('choice', 'icon')


@admin.register(Question)
class QuestionAdmin(TranslationAdmin):
    list_display = ('id', 'question', 'type')
    search_fields = ('question',)
    inlines = (ChoiceOfMultipleChoiceQuestionInline,)


@admin.register(ChoiceOfMultipleChoiceQuestion)
class ChoiceOfMultipleChoiceQuestionAdmin(TranslationAdmin):
    list_display = ('id', 'question', 'choice')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id',)
    filter_horizontal = ('questions',)


@admin.register(FileAnswer)
class FileAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')


@admin.register(DescriptiveAnswer)
class DescriptiveAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')


@admin.register(MultipleChoiceAnswer)
class MultipleChoiceAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')


@admin.register(UserExam)
class UserExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'exam')
