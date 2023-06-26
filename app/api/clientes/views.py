from rest_framework.permissions import (
    DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, IsAdminUser)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ClienteSerializer
from .models import Cliente


class ListClientes(APIView):
    """Lista todos los clientes, esta vista solo puede
    ser accedida port usuarios administradores."""

    queryset = Cliente.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly, 
                          IsAuthenticated, 
                          IsAdminUser]
    permission_groups = ['admin']
    
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)


class DetailCliente(APIView):
    """Muesta los detalles de un cliente."""
    
    queryset = Cliente.objects.all()
    permission_classes = ['admin']
    
    def get(self, request, pk):
        cliente = Cliente.objects.get(pk=pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)


class CreateCliente(APIView):

    permission_classes = [IsAdminUser, IsAuthenticated]
    permission_groups = ['admin']
    
    def post(self, request):
        """Crea un nuevo cliente."""
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)