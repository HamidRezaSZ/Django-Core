from disposable_email_domains import blocklist
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.serializers import Serializer

from accounts.models import User
from base.serializers.base_serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """
    User serializers for register
    """

    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = (
            "user_permissions",
            "groups",
            "date_joined",
            "is_active",
            "is_superuser",
            "last_login",
            "is_staff",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        elif attrs["email"].split("@")[1] in blocklist:
            raise serializers.ValidationError({"email": "The email domain is blocked."})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)

        return user


class ChangePasswordSerializer(ModelSerializer):
    """
    User change password serializers
    """

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return super().validate(attrs)

    def update(self, instance, validated_data):
        if not instance.check_password(validated_data["old_password"]):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )

        instance.set_password(validated_data["password"])
        instance.save()

        return instance


class PhoneNumberSerializer(Serializer):
    """
    Serializer for phone number
    """

    phone_validator = RegexValidator(
        regex=r"^(09|9)\d{9}$",
        message="Start with 09/9 and it must 9 digits after that. For example: 0912000000 or 9120000000",
    )
    phone_number = serializers.CharField(validators=[phone_validator])
