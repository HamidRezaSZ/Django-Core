from modeltranslation.translator import TranslationOptions, translator

from .models import *


class CourseCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ChapterTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class NoteTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(CourseCategory, CourseCategoryTranslationOptions)
translator.register(Course, CourseTranslationOptions)
translator.register(Lesson, LessonTranslationOptions)
translator.register(Chapter, ChapterTranslationOptions)
translator.register(Note, NoteTranslationOptions)
