from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from rest_framework import serializers

from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = ('id', 'nombre', 'apellidos', 'telefono', 'email')

    def save(self, **kwargs):
        
        # primero creamos el usuario de Django si no existe
        # Nota: después de inverstigar la web publica de reclamador
        # he visto que se solicita una contraseña en el mismo paso
        # del proceso de registro de una reclamación, por lo que
        # he decidido no incluir intencionalmente la contraseña en
        # el registro de un cliente por simplicidad ya que no se solicita en 
        # el documento de requerimientos, por lo tanto
        # el password va en hard code en el código.
        user = User.objects.create_user(
            username=self.validated_data['email'],
            email=self.validated_data['email'],
            password="123456"
        )
        # añadimos el usuario al grupo crrespondiente
        grupo_cliente = Group.objects.get(name='cliente')
        user.groups.add(grupo_cliente)

        cliente = Cliente(
            user=user,
            nombre=self.validated_data['nombre'],
            apellidos=self.validated_data['apellidos'],
            telefono=self.validated_data['telefono'],
            email=self.validated_data['email']
        )

        cliente.save()

        return cliente