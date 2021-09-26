from django.contrib.auth.models import User
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                                  style={'input_type': 'password', 'placeholder': 'Password'})
    password_confirmation = serializers.CharField(write_only=True,
                                                  style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_confirmation']


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']