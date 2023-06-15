from django.shortcuts import get_object_or_404
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import Response

from base.viewsets import ModelViewSet

from .models import Profile
from .serializers import *
from .utils import create_OTP, send_otp_sms


class Register(CreateAPIView):
    serializer_class = UserSerializer


class ChangePasswordView(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user


class GetPhoneNumberRegistered(GenericAPIView):
    serializer_class = PhoneNumberSerializer

    def post(self, request) -> Response:
        phone_serializer = PhoneNumberSerializer(data=request.data)
        phone_serializer.is_valid(raise_exception=True)
        phone = phone_serializer.validated_data['phone_number']
        OTP = create_OTP(phone)

        response = send_otp_sms(OTP, phone)

        if response:
            return Response({'message': 'SMS sent'}, status=200)

        return Response({"message": 'Error while sending SMS!'}, status=400)


class ProfileView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAdminUser],
    }

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ProfileGetSerializer

        return ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context


class AddressesView(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AddressGetSerializer

        return AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Address, user=self.request.user, pk=pk)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context
