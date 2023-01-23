from .views import CartView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', CartView, basename='cart')

urlpatterns = router.urls
