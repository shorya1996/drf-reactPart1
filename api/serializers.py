from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fname', 'password', 'username']


class LoginDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userid', 'email', 'fname', 'username']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']