from django.contrib import admin
from django.urls import path, include

from api.clientes import urls as clientes_urls
from api.reclamaciones import urls as reclamaciones_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/clientes/', include(clientes_urls)),
    path('api/v1/reclamaciones/', include(reclamaciones_urls)),
]
