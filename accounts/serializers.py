from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password
from disposable_email_domains import blocklist
from django.core.validators import RegexValidator
from base.serializers import CityGetSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    User serializers for register
    """

    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = ('user_permissions', 'groups', 'date_joined', 'is_active', 'is_superuser', 'last_login', 'is_staff')

    def create(self, validated_data):
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        elif validated_data['email'].split('@')[1] in blocklist:
            raise serializers.ValidationError({"email": "The email domain is blocked."})

        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    User change password serializers
    """

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True, allow_null=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def update(self, instance, validated_data):
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        if not instance.check_password(validated_data['old_password']):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class PhoneNumberSerializer(serializers.Serializer):
    """
    Serializer for phone number
    """

    phone_validator = RegexValidator(
        regex=r'^(09|9)\d{9}$',
        message='Start with 09/9 and it must 9 digits after that. For example: 0912000000 or 912000000000')
    phone_number = serializers.CharField(validators=[phone_validator])


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('related_user',)

    def update(self, instance, validated_data):
        user = self.context.get('user')
        validated_data['related_user'] = user

        return super().update(instance, validated_data)


class ProfileGetSerializer(serializers.ModelSerializer):
    related_city = CityGetSerializer()

    class Meta:
        model = Profile
        exclude = ('related_user',)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ('related_user',)

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['related_user'] = user
        return super().create(validated_data)


class AddressGetSerializer(serializers.ModelSerializer):
    city = CityGetSerializer()

    class Meta:
        model = Address
        exclude = ('related_user',)
