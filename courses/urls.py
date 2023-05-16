from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'category', CourseCategoryView)
router.register(r'course', CourseView)
router.register(r'lesson', LessonView)
router.register(r'chapter', ChapterView)
router.register(r'note', NoteView, basename='note')
router.register(r'note-taking', NoteTakingView, basename='note_taking')

urlpatterns = router.urls
