from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order-quantities', OrderProductQuantityViewSet, basename='order-quantities')
router.register(r'delivery-types', DeliveryTypeViewSet)

urlpatterns = router.urls
