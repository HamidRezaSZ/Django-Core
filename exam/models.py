from django.db import models
from base.models import BaseModel
from accounts.models import User


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
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='سوال مربوطه')
    icon = models.FileField(null=True, blank=True, verbose_name='آیکون')
    choice = models.CharField(max_length=200, verbose_name='مقدار')
    is_true = models.BooleanField(default=False, verbose_name='جواب درست')

    class Meta:
        verbose_name = 'گزینه سوال چند گزینه ای'
        verbose_name_plural = 'گزینه های سوال چند گزینه ای'


class DescriptiveAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='سوال مربوطه')
    answer = models.TextField(verbose_name='پاسخ')

    class Meta:
        verbose_name = 'جواب تشریحی'
        verbose_name_plural = 'جواب های تشریحی'


class MultipleChoiceAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='سوال مربوطه')
    answer = models.ForeignKey(ChoiceOfMultipleChoiceQuestion, on_delete=models.PROTECT, verbose_name='پاسخ')

    class Meta:
        verbose_name = 'جواب چند گزینه ای'
        verbose_name_plural = 'جواب های چند گزینه ای'


class FileAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name='سوال مربوطه')
    answer = models.FileField(verbose_name='فایل پاسخ')

    class Meta:
        verbose_name = 'فایل جواب'
        verbose_name_plural = 'فایل های جواب'


class Exam(BaseModel):
    questions = models.ManyToManyField(Question, verbose_name='سوالات')

    class Meta:
        verbose_name = 'آزمون'
        verbose_name_plural = 'آزمون ها'


class UserExam(models.Model):
    user = models.ForeignKey(to=User, verbose_name='کاربر', on_delete=models.CASCADE)
    exam = models.ForeignKey(to=Exam, verbose_name='آزمون', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'آزمون کاربر'
        verbose_name_plural = 'آزمون های کاربر'
