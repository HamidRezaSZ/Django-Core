from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)
from .views import *
from rest_framework.routers import DefaultRouter

app_name = "accounts"

router = DefaultRouter()


router.register(r'addresses', AddressesView, basename='addresses')
router.register(r'profile', ProfileView, basename='profile')

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path("otp/", GetPhoneNumberRegistered.as_view(), name="OTP_Gen"),
] + router.urls
