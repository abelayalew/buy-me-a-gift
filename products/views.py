from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from . import serializers, models


class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = []

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ProductBasicSerializer
        return serializers.ProductSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        _objects = models.Product.objects.filter()

        try:
            if price_lt := query_params.get('price_lt'):
                _objects = _objects.filter(price__lt=float(price_lt))

            if price_gt := query_params.get('price_gt'):
                _objects = _objects.filter(price__gt=float(price_gt))
        except ValueError:
            raise ValidationError("invalid filter parameter")

        return _objects

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

