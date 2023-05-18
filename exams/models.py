from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from base.models import BaseModel


class Exam(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey(
        to='self', on_delete=models.CASCADE, verbose_name=_('parent'), null=True, blank=True, related_name='child')
    minimum_score = models.PositiveIntegerField(
        verbose_name=_('minimum_score'))
    duration = models.DurationField(verbose_name=_('duration'))
    wrong_questions_weight = models.PositiveIntegerField(
        default=3, verbose_name=_('wrong_questions_weight'))
    correct_questions_weight = models.PositiveIntegerField(
        default=1, verbose_name=_('correct_questions_weight'))

    class Meta:
        verbose_name = _('Exam')
        verbose_name_plural = _('Exams')
        ordering = ('created_date', 'title')

    def __str__(self) -> str:
        return self.title

    def remaining_time(self, user) -> int:
        date = UserExam.objects.get(user__id=user, exam=self).created_date
        remaning = date + self.duration - timezone.now()
        if remaning.total_seconds() > 0:
            return remaning.total_seconds()
        return 0


class UserExam(BaseModel):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name=_('user'))
    exam = models.ForeignKey(to=Exam, verbose_name=_(
        'exam'), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('User Exam')
        verbose_name_plural = _('User Exams')

    def __str__(self) -> str:
        return f'{self.exam}'


class Question(BaseModel):
    CORRECT_ANSWER = [(int(x), str(x)) for x in range(1, 5)]

    exam = models.ForeignKey(to=Exam, verbose_name=_(
        'exam'), on_delete=models.PROTECT)
    title = models.CharField(max_length=200, verbose_name=_(
        'title'), null=True, blank=True)
    question = models.TextField(verbose_name=_('question'))
    choice_one = models.TextField(verbose_name=_('choice_one'))
    choice_two = models.TextField(verbose_name=_('choice_two'))
    choice_three = models.TextField(verbose_name=_('choice_three'))
    choice_four = models.TextField(verbose_name=_('choice_four'))
    correct_answer = models.IntegerField(
        choices=CORRECT_ANSWER, verbose_name=_('correct_answer'))

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self) -> str:
        return f'{self.question}'


class DescriptiveAnswer(BaseModel):
    exam = models.OneToOneField(to=Exam, verbose_name=_(
        'exam'), on_delete=models.CASCADE)
    content = RichTextUploadingField(verbose_name=_('content'))

    class Meta:
        verbose_name = _('Descriptive Answer')
        verbose_name_plural = _('Descriptive Answers')

    def __str__(self) -> str:
        return f'{self.exam}'


class UserQuestion(BaseModel):
    ANSWER = [(int(x), str(x)) for x in range(1, 5)]

    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name=_('user'))
    exam = models.ForeignKey(to=Exam, verbose_name=_(
        'exam'), on_delete=models.PROTECT)
    question = models.ForeignKey(to=Question, on_delete=models.PROTECT)
    answer = models.IntegerField(choices=ANSWER, verbose_name=_('answer'))

    class Meta:
        verbose_name = _('User Question')
        verbose_name_plural = _('User Questions')

    def __str__(self) -> str:
        return f'{self.user} - {self.question} - {self.answer}'


class Result(BaseModel):
    user = models.ForeignKey(
        to='accounts.User', on_delete=models.CASCADE, verbose_name=_('user'))
    exam = models.ForeignKey(
        to=Exam, on_delete=models.CASCADE, verbose_name=_('exam'))
    parent = models.ForeignKey(
        to='self', on_delete=models.CASCADE, verbose_name=_('parent'), null=True, blank=True, related_name='child')
    no_all_questions = models.PositiveIntegerField(
        verbose_name=_('no_all_questions'))
    no_wrong_questions = models.PositiveIntegerField(
        verbose_name=_('no_wrong_questions'))
    no_correct_questions = models.PositiveIntegerField(
        verbose_name=_('no_correct_questions'))
    max_score = models.FloatField(default=0, verbose_name=_('max_score'))
    score = models.FloatField(default=0, verbose_name=_('score'))

    class Meta:
        verbose_name = _('Result')
        verbose_name_plural = _('Results')

    def __str__(self) -> str:
        return f'{self.user} - {self.exam}'
