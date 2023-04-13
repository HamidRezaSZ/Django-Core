from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'cart',CartView, basename='cart')
router.register(r'cart-item', CartItemView, basename='cart_item')

urlpatterns = router.urls
