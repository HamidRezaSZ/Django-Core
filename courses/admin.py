from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from .models import *


@admin.register(CourseCategory)
class CourseCategoryAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'show_on_home_page', 'is_active')
    list_editable = ('show_on_home_page', 'is_active')
    search_fields = ('title', 'description')


class LessonInline(TranslationStackedInline):
    model = Lesson
    extra = 0


class ChapterInline(TranslationStackedInline):
    model = Chapter
    extra = 0


class NoteInline(TranslationStackedInline):
    model = Note
    extra = 0
    filter_horizontal = ('participants',)


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'category', 'price', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'description')
    inlines = (LessonInline,)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Lesson)
class LessonAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'course', 'price', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'description')
    inlines = (ChapterInline,)


@admin.register(Chapter)
class ChapterAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'lesson', 'price', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title',)
    inlines = (NoteInline,)


@admin.register(Note)
class NoteAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'chapter', 'price',
                    'show_on_home_page', 'is_active')
    list_editable = ('show_on_home_page', 'is_active',)
    filter_horizontal = ('participants',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_active')
    list_editable = ('is_active',)


@admin.register(NoteTaking)
class NoteTakingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'note')
