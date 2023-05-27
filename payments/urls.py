from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'payment', PaymentView, basename='payment')
router.register(r'payment-gateways', PaymentGateWayView,
                basename='payment-gateway')

urlpatterns = [
    path('verify/', VerifyPayment.as_view(), name='verify'),
] + router.urls
