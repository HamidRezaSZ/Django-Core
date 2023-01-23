from rest_framework.routers import DefaultRouter
from .views import PaymentView, VerifyPayment
from django.urls import path

router = DefaultRouter()
router.register(r'payment', PaymentView, basename='payment')

urlpatterns = [
    path('verify/<str:authority>/<str:status>/', VerifyPayment.as_view(), name='verify'),
] + router.urls
