from django.contrib import admin
from .models import *


class ChoiceOfMultipleChoiceQuestionInline(admin.TabularInline):
    model = ChoiceOfMultipleChoiceQuestion
    extra = 0
    fields = ('choice', 'icon')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'type')
    inlines = (ChoiceOfMultipleChoiceQuestionInline,)


@admin.register(ChoiceOfMultipleChoiceQuestion)
class ChoiceOfMultipleChoiceQuestionAdmin(admin.ModelAdmin):
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
