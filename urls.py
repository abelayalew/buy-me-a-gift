from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="BUY ME A GIFT API",
      default_version='v1',
      description="Vinhood store",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('products.urls')),
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='docs')
]
