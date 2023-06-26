from django.urls import path, include

from .views import ReclamacionCreate, ReclamacionDetail

urlpatterns = [
    path('create/', ReclamacionCreate.as_view(), name='reclamacion-create'),
    path('<int:pk>/', ReclamacionDetail.as_view(), name='reclamacion-detail'),
]