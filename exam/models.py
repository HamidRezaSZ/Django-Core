from django.db import models
from base.models import BaseModel


class Question(BaseModel):
    class Type(models.TextChoices):
        MULTIPLECHOICE = 'MultipleChoice', 'چند گزینه ای'
        DROPDOWN = 'Drop Down', 'کشویی'
        FILE = 'File', 'فایل'
        DESCRIPTIVE = 'Descriptive', 'تشریحی'

    question = models.TextField(verbose_name='سوال')
    type = models.CharField(max_length=20, choices=Type.choices, default='Descriptive', verbose_name='نوع سوال')

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'


class ChoiceOfMultipleChoiceQuestion(BaseModel):
    related_question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='سوال مربوطه')
    icon = models.FileField(null=True, blank=True, verbose_name='آیکون')
    choice = models.CharField(max_length=200, verbose_name='مقدار')

    class Meta:
        verbose_name = 'مقدار سوال چند گزینه ای'
        verbose_name_plural = 'مقدار های سوال چند گزینه ای'


class DescriptiveAnswer(models.Model):
    related_question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='سوال مربوطه')
    answer = models.TextField(verbose_name='پاسخ')

    class Meta:
        verbose_name = 'جواب تشریحی'
        verbose_name_plural = 'جواب های تشریحی'


class MultipleChoiceAnswer(models.Model):
    related_question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='سوال مربوطه')
    answer = models.ForeignKey(ChoiceOfMultipleChoiceQuestion, on_delete=models.PROTECT, verbose_name='پاسخ')

    class Meta:
        verbose_name = 'جواب چند گزینه ای'
        verbose_name_plural = 'جواب های چند گزینه ای'


class FileAnswer(models.Model):
    related_question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='سوال مربوطه')
    answer = models.FileField(verbose_name='فایل پاسخ')

    class Meta:
        verbose_name = 'فایل جواب'
        verbose_name_plural = 'فایل های جواب'


class Exam(BaseModel):
    related_questions = models.ManyToManyField(Question, verbose_name='سوالات')

    class Meta:
        verbose_name = 'آزمون'
        verbose_name_plural = 'آزمون ها'
