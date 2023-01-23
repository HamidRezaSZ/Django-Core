from rest_framework.routers import DefaultRouter
from .views import NewsLettersView

app_name = "newsletters"

router = DefaultRouter()

router.register(r'register', NewsLettersView)


urlpatterns = router.urls
