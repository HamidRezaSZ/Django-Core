from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class CourseCategory(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    icon = models.FileField(upload_to='product-category-icon',
                            verbose_name=_('icon'), null=True, blank=True)
    image_alt = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextUploadingField(
        verbose_name=_('description'), null=True, blank=True)
    show_on_home_page = models.BooleanField(
        default=False, verbose_name=_('show_on_home_page'))
    meta_title = models.CharField(max_length=128, verbose_name=_(
        'meta_title'), null=True, blank=True)
    meta_description = models.TextField(verbose_name=_(
        'meta_description'), null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Teacher(BaseModel):
    user = models.ForeignKey(
        to='accounts.User', on_delete=models.CASCADE, verbose_name=_('user'))

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')


class Course(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    slug = models.SlugField(unique=True)
    teacher = models.ForeignKey(
        to=Teacher, on_delete=models.PROTECT, verbose_name=_('teacher'))
    category = models.ForeignKey(to=CourseCategory, verbose_name=_(
        'category'), on_delete=models.CASCADE)
    image = models.FileField(verbose_name=_(
        'image'), upload_to='course-images')
    image_alt = models.CharField(max_length=200, null=True, blank=True)
    video = models.FileField(verbose_name=_(
        'video'), upload_to='course-videos', null=True, blank=True)
    cover = models.FileField(verbose_name=_(
        'cover'), upload_to='course-covers', null=True, blank=True)
    description = RichTextUploadingField(verbose_name=_('description'))
    price = models.PositiveIntegerField(verbose_name=_('price'))
    for_sale = models.BooleanField(default=True, verbose_name=_('for_sale'))

    def __str__(self) -> str:
        return self.title

    def full_access_user(self, user) -> bool:
        lessons = self.lesson_set.all(
        ).values_list('id', flat=True)
        chapters = Lesson.objects.filter(
            id__in=lessons).values_list('chapter', flat=True)
        notes = Chapter.objects.filter(
            id__in=chapters).values_list('note', flat=True)
        if set(notes) == set(Note.objects.filter(participants=user, chapter__in=chapters).values_list('id', flat=True)):
            return True
        return False

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')


class Lesson(BaseModel):
    course = models.ForeignKey(to=Course, verbose_name=_(
        'course'), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('title'))
    image = models.FileField(upload_to='lesson-images')
    image_alt = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextUploadingField(verbose_name=_('description'))
    price = models.PositiveIntegerField(verbose_name=_('price'))
    for_sale = models.BooleanField(default=True, verbose_name=_('for_sale'))

    def __str__(self) -> str:
        return f'{self.title} - {self.course.title}'

    def full_access_user(self, user) -> bool:
        chapters = self.chapter_set.all(
        ).values_list('id', flat=True)
        notes = Chapter.objects.filter(
            id__in=chapters).values_list('note', flat=True)
        if set(notes) == set(Note.objects.filter(participants=user, chapter__in=chapters).values_list('id', flat=True)):
            return True
        return False

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')


class Chapter(BaseModel):
    lesson = models.ForeignKey(to=Lesson, verbose_name=_(
        'lesson'), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('title'))
    image = models.FileField(upload_to='chapter-images')
    image_alt = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextUploadingField(verbose_name=_('description'))
    price = models.PositiveIntegerField(verbose_name=_('price'))
    for_sale = models.BooleanField(default=True, verbose_name=_('for_sale'))

    def __str__(self) -> str:
        return f'{self.title} - {self.lesson.title} - {self.lesson.course.title}'

    def full_access_user(self, user) -> bool:
        if set(self.note_set.all().values_list('id', flat=True)) == set(Note.objects.filter(participants=user, chapter=self).values_list('id', flat=True)):
            return True
        return False

    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')


class Note(BaseModel):
    chapter = models.ForeignKey(to=Chapter, verbose_name=_(
        'chapter'), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=_('title'))
    price = models.PositiveIntegerField(verbose_name=_('price'))
    image = models.FileField(upload_to='note-images')
    image_alt = models.CharField(max_length=200, null=True, blank=True)
    content = RichTextUploadingField(verbose_name=_('content'))
    for_sale = models.BooleanField(default=True, verbose_name=_('for_sale'))
    participants = models.ManyToManyField(
        to='accounts.User', verbose_name=_('participants'), null=True, blank=True)
    show_on_home_page = models.BooleanField(
        default=False, verbose_name=_('show_on_home_page'))

    def __str__(self) -> str:
        return f'{self.title} - {self.chapter.title} - {self.chapter.lesson.title} - {self.chapter.lesson.course.title}'

    def add_to_participants(self, user):
        self.participants.add(user)

    def full_access_user(self, user) -> bool:
        if user in self.participants.all():
            return True
        return False

    def remove_from_participants(self, user):
        self.participants.remove(user)

    class Meta:
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')


class NoteTaking(models.Model):
    note = models.ForeignKey(to=Note, on_delete=models.CASCADE, verbose_name=_(
        'note'))
    user = models.ForeignKey(
        to='accounts.User', on_delete=models.CASCADE, verbose_name=_('user'))
    content = RichTextUploadingField(verbose_name=_('content'))

    def __str__(self) -> str:
        return f'{self.user - self.note}'

    class Meta:
        verbose_name = _('Note Taking')
        verbose_name_plural = _('Note Taking')
