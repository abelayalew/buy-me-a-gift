from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
from . import serializers, models


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = []

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise AuthenticationFailed()

        return super().post(request, *args, **kwargs)


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()

    def check_permissions(self, request):
        authenticated = request.user.is_authenticated
        method = request.method

        if not authenticated and method == 'GET':
            return True

        raise AuthenticationFailed()

