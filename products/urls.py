from django.urls import path
from . import views


prefix = 'products'


urlpatterns = [
    path('products', views.ProductListCreateView.as_view()),
    path('product/<pk>', views.ProductRetrieveUpdateDestroyView.as_view()),
]
