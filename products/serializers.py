from rest_framework import serializers
from . import models


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = 'name',


class ProductBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = 'id', 'name', 'price', 'category', 'created_at'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WishList
        fields = '__all__'
