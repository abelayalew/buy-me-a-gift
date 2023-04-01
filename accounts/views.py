from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
from . import models, serializers


class LoginView(generics.CreateAPIView):
    serializer_class = serializers.LoginSerializer
    permission_classes = []


class SignupView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = []


class PasswordResetView(generics.CreateAPIView):
    serializer_class = serializers.PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        user = request.user

        if not user.check_password(validated_data.get('old_password')):
            raise AuthenticationFailed("please enter correct password")

        if validated_data.get('new_password_1') != validated_data.get('new_password_2'):
            raise ValidationError("New Password mismatch")

        user.set_password(validated_data.get('new_password_1'))
        user.save()

        data = serializers.LoginSerializer(instance={'user': user, **serializers.LoginSerializer.generate_token(user)})

        return Response(data.data)

