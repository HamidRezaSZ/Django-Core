from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from base.models import BaseModel


class Question(BaseModel):
    TYPE = (
        ('MultipleChoice', 'MultipleChoice'),
        ('Drop Down', 'Drop Down'),
        ('File', 'File'),
        ('Descriptive', 'Descriptive'),
    )

    question = models.TextField(verbose_name=_('question'))
    type = models.CharField(max_length=20, choices=TYPE, default='Descriptive', verbose_name=_('type'))

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')


class ChoiceOfMultipleChoiceQuestion(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name=_('question'))
    icon = models.FileField(null=True, blank=True, verbose_name=_('icon'))
    choice = models.CharField(max_length=200, verbose_name=_('choice'))
    is_true = models.BooleanField(default=False, verbose_name=_('is_true'))

    class Meta:
        verbose_name = _('Choice Of MultipleChoice Question')
        verbose_name_plural = _('Choices Of MultipleChoice Question')


class DescriptiveAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name=_('question'))
    answer = models.TextField(verbose_name=_('answer'))

    class Meta:
        verbose_name = _('Descriptive Answer')
        verbose_name_plural = _('Descriptive Answers')


class MultipleChoiceAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name=_('question'))
    answer = models.ForeignKey(ChoiceOfMultipleChoiceQuestion, on_delete=models.PROTECT, verbose_name=_('answer'))

    class Meta:
        verbose_name = _('Multiple Choice Answer')
        verbose_name_plural = _('Multiple Choice Answers')


class FileAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name=_('question'))
    answer = models.FileField(verbose_name=_('answer'))

    class Meta:
        verbose_name = _('File Answer')
        verbose_name_plural = _('File Answers')


class Exam(BaseModel):
    questions = models.ManyToManyField(Question, verbose_name=_('questions'))

    class Meta:
        verbose_name = _('Exam')
        verbose_name_plural = _('Exams')


class UserExam(models.Model):
    user = models.ForeignKey(to=User, verbose_name=_('user'), on_delete=models.CASCADE)
    exam = models.ForeignKey(to=Exam, verbose_name=_('exam'), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('User Exam')
        verbose_name_plural = _('User Exams')
