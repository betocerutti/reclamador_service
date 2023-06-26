from django.shortcuts import render
from django.http import Http404

from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, IsAdminUser)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ReclamacionSerializer
from .models import Reclamacion


class ReclamacionCreate(APIView):
    """
    Crea una nueva reclamación, solo los clientes pueden crear reclamaciones.
    """
    permission_classes = [IsAuthenticated]
    permission_groups = ['cliente']
    
    def post(self, request):
        """Crea un nuevo cliente."""
        serializer = ReclamacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ReclamacionDetail(APIView):
    """
    Recupera una reclamacion, solo los clientes pueden ver sus reclamaciones.
    """
    permission_classes = [IsAuthenticated]
    permission_groups = ['cliente']
    
    def get_object(self, pk):
        try:
            return Reclamacion.objects.get(pk=pk)
        except Reclamacion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reclamacion = self.get_object(pk)
        serializer = ReclamacionSerializer(reclamacion)
        return Response(serializer.data)