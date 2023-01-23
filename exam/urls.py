from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'answers/multiple-choice', MultipleChoiceAnswerView)
router.register(r'answers/descriptive', DescriptiveAnswerView)
router.register(r'answers/file', FileAnswerView)
router.register(r'', ExamView)

urlpatterns = router.urls
