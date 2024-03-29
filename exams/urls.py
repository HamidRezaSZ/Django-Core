from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'exam', ExamView, basename='exam')
router.register(r'descriptive-answer', DescriptiveAnswerView,
                basename='descriptive-answer')
router.register(r'user-answer', UserAnswerView, basename='user-answer')
router.register(r'result', ResultView, basename='result')

urlpatterns = router.urls
