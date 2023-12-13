from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import serializers
import re

from .models import *


class UserSerializer(ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        # Add more fields as needed
        fields = ('id', 'username', 'email', 'password')
        # Password should not be read
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError(
                "Password must be at least 6 characters long.")
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError(
                "Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9!@#$%^&*()_+=-]', value):
            raise serializers.ValidationError(
                "Password must contain at least one number or symbol.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("An account with that Email already exists!")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token, created = Token.objects.get_or_create(user=user)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
