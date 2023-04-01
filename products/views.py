from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from . import serializers, models
from accounts.models import User

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


class WishListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.WishListSerializer

    def get_queryset(self):
        q_params = self.request.query_params

        if user_id := q_params.get('user'):
            return models.WishList.objects.filter(user_id=user_id)

        return models.WishList.objects.filter(user=self.request.user)

    def check_permissions(self, request):
        authenticated = request.user.is_authenticated
        q_params = request.query_params

        if user_id := q_params.get('user'):
            try:
                User.objects.get(id=user_id)
                return True
            except User.DoesNotExist:
                raise ValidationError("please provide a valid user id")

        if not authenticated:
            raise AuthenticationFailed("Please login or provide a valid user id")


class WishRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.WishListSerializer
    queryset = models.WishList.objects.all()


class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.ProductCategorySerializer
    queryset = models.ProductCategory.objects.all()

    def check_permissions(self, request):
        if request.method == 'GET':
            return True


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductCategorySerializer
    queryset = models.ProductCategory.objects.all()

    def check_permissions(self, request):
        if request.method == 'GET':
            return True
