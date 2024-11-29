from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response

from accounts.serializers.user import (
    ChangePasswordSerializer,
    PhoneNumberSerializer,
    UserSerializer,
)
from accounts.utils.otp import create_OTP, send_otp_sms


class Register(CreateAPIView):
    serializer_class = UserSerializer


class ChangePasswordView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user


class GetPhoneNumberRegistered(GenericAPIView):
    serializer_class = PhoneNumberSerializer

    def post(self, request) -> Response:
        phone_serializer = PhoneNumberSerializer(data=request.data)
        phone_serializer.is_valid(raise_exception=True)
        phone = phone_serializer.validated_data["phone_number"]
        OTP = create_OTP(phone)

        response = send_otp_sms(OTP, phone)

        if response:
            return Response({"message": "SMS sent"}, status=200)

        return Response({"message": "Error while sending SMS!"}, status=400)
