from rest_framework import generics
from rest_framework.response import Response
from . import models, serializers


class LoginView(generics.CreateAPIView):
    serializer_class = serializers.LoginSerializer
    permission_classes = []


class SignupView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = []
