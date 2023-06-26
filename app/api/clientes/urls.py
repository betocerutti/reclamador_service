from django.urls import path, include

from .views import ListClientes, DetailCliente, CreateCliente

urlpatterns = [
    path('', ListClientes.as_view(), name='cliente-list'),
    path('create/', CreateCliente.as_view(), name='cliente-create'),
    path('<int:pk>/', DetailCliente.as_view(), name='cliente-detail'),
]
