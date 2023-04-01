from django.urls import path
from . import views


urlpatterns = [
    path('products', views.ProductListCreateView.as_view()),
    path('product/<pk>', views.ProductRetrieveUpdateDestroyView.as_view()),
    path('wish-lists', views.WishListCreateView.as_view()),
    path('wish-list/<pk>', views.WishRetrieveUpdateDestroyView.as_view()),
]
