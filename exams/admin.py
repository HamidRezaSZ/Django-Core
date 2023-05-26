from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from .models import *


class DescriptiveAnswerInline(TranslationStackedInline):
    model = DescriptiveAnswer


class QuestionInline(TranslationStackedInline):
    model = Question
    extra = 0


@admin.register(Exam)
class ExamAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')
    list_editable = ('is_active',)
    inlines = (DescriptiveAnswerInline, QuestionInline)


@admin.register(Question)
class QuestionAdmin(TranslationAdmin):
    list_display = ('id', 'exam', 'question', 'is_active')
    list_editable = ('is_active',)


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'exam', 'question')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'exam', 'parent', 'score')


@admin.register(UserExam)
class UserExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'exam')
