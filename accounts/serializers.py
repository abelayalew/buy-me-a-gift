from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = 'groups',
        extra_kwargs = {
            'password': {'write_only': True}
        }


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    user = UserSerializer(read_only=True)
    token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    @classmethod
    def generate_token(cls, user):
        refresh_token = RefreshToken.for_user(user)

        return {
            'token': refresh_token.access_token.__str__(),
            'refresh_token': refresh_token.__str__()
        }

    def create(self, validated_data):
        user = authenticate(email=validated_data.get('email'), password=validated_data.get('password'))

        if not user:
            raise AuthenticationFailed()

        return {
            'user': user,
            **self.generate_token(user)
        }


class PasswordResetSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password_1 = serializers.CharField(write_only=True)
    new_password_2 = serializers.CharField(write_only=True)
