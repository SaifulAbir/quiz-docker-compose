from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user import models as user_models
from user.models import *


class OTPSendSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {"contact_number": {"required": True}}
        fields = "__all__"
        model = OTPModel


class OTPReSendSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {"contact_number": {"required": True}}
        fields = ("contact_number",)
        model = OTPModel


class OTPVerifySerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "contact_number": {"required": True},
            "otp_number": {"required": True},
        }
        fields = ("contact_number", "otp_number")
        model = OTPModel


class LoginSerializer(serializers.Serializer):
    """
    Serializer for login endpoint.
    """

    phone = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "last_login",
            "full_name",
            "email",
            "phone",
            "gender",
            "address",
            "age",
            "life",
            "hint",
            "level",
            "point",
            "is_active",
            "is_staff",
            "is_superuser",
            "verified_email",
            "date_joined",
        )
