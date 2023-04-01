from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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
        fields = 'product',

    def create(self, validated_data):
        user = self.context['request'].user

        existing_records = models.WishList.objects.filter(
            product__category=validated_data.get('product').category
        )

        if existing_records:
            raise ValidationError("you can not have more than one record with the same category")

        validated_data['user'] = user
        return super().create(validated_data)
