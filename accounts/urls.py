from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views.address import AddressesView
from accounts.views.profile import ProfileView
from accounts.views.user import ChangePasswordView, GetPhoneNumberRegistered, Register

app_name = "accounts"

router = DefaultRouter()


router.register(r"addresses", AddressesView, basename="addresses")
router.register(r"profile", ProfileView, basename="profile")

urlpatterns = [
    path("register/", Register.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("change_password/", ChangePasswordView.as_view()),
    path("otp/", GetPhoneNumberRegistered.as_view(), name="OTP_Gen"),
] + router.urls
