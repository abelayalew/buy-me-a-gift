from django.db import models
from lib.mixins import BaseModelMixin, NULL


class ProductCategory(BaseModelMixin):
    name = models.CharField(unique=True, max_length=100)


class Product(BaseModelMixin):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, models.CASCADE, related_name='products')
    price = models.FloatField()
    rank = models.IntegerField(default=0)

    class Meta:
        ordering = 'rank', 'created_at'


class WishList(BaseModelMixin):
    user = models.ForeignKey('accounts.User', models.CASCADE, 'wishlist')
    product = models.ForeignKey(Product, models.CASCADE)
