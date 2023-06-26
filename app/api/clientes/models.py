import re

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_mobile_phone(value):
    """
    Se define una función que valida que el teléfono móvil tenga el formato correcto.
    """
    pattern = r'^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    if not re.match(pattern, value):
        raise ValidationError('El número de teléfono móvil no es válido.')

class Cliente(models.Model):
    """
    Se decide crear un modelo Cliente con una relación 1:1 con el modelo User
    para poder crear usuarios de Django que no sean clientes, como por ejemplo 
    administradores.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    telefono = models.CharField(max_length=20, validators=[validate_mobile_phone])

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellidos)
