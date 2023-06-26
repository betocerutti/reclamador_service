from django.test import TestCase
from django.contrib.auth.models import User

from .models import Cliente


class TestCliente(TestCase):
    """
    Se definen los tests para el modelo Cliente.
    """
    def setUp(self):
        """
        Se define un cliente para los tests.
        """
        # primero creamos un usuario de Django
        self.user = User.objects.create_user(
            username="test",
            password="test"
        )
        # luego creamos un cliente
        self.cliente = Cliente.objects.create(
            user=self.user,
            nombre="Test",
            apellidos="Test",
            email="yo@gmail.com",
            telefono="+34 123456789"
        )
    
    def test_cliente_object_creation(self):
        """
        Se comprueba que el cliente se ha creado correctamente.
        """
        self.assertTrue(isinstance(self.cliente, Cliente))
        self.assertEqual(self.cliente.__str__(), "Test Test")

