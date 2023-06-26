from django.contrib import admin
from django.urls import path, include

from api.clientes import urls as clientes_urls
from api.reclamaciones import urls as reclamaciones_urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Reclamador API",
      default_version='v1',
      description="Prueba técnica para Reclamador.es",
      terms_of_service="https://www.example.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/clientes/', include(clientes_urls)),
    path('api/v1/reclamaciones/', include(reclamaciones_urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
