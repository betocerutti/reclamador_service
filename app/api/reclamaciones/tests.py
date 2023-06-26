from datetime import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone

from api.clientes.models import Cliente
from .models import Reclamacion


class TestReclamacion(TestCase):
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
        # luego creamos una reclamación

        self.reclamacion = Reclamacion.objects.create(
            cliente=self.cliente,
            fecha_vuelo=timezone.make_aware(datetime.now(), timezone.get_current_timezone()),
            numero_vuelo="IB1234",
            aeropuerto_salida="MAD",
            aeropuerto_llegada="BCN",
            nombre_aerolinea="Iberia"
        )

    def test_reclamacion_object_creation(self):
        """
        Se comprueba que la reclamación se ha creado correctamente.
        """
        self.assertTrue(isinstance(self.reclamacion, Reclamacion))
        self.assertEqual(self.reclamacion.__str__(), 
                         "Reclamación de {} para el vuelo {} de {}".format(
                             self.cliente.email,
                             self.reclamacion.numero_vuelo,
                             self.reclamacion.fecha_vuelo)
                         )
        
    def test_reclamacion_get_absolute_url(self):
        """
        Se comprueba que la reclamación tiene un método get_absolute_url
        """
        self.assertIsNotNone(self.reclamacion.get_absolute_url())

    def test_reclamacion_inicializar(self):
        """
        Se comprueba que la reclamación se inicializa correctamente.
        """
        self.reclamacion.inicializar()
        self.assertIsNotNone(self.reclamacion.numero_expediente)
        self.assertIsNotNone(self.reclamacion.fecha_vista)
        self.assertIsNotNone(self.reclamacion.cantidad_reclamada)
        self.assertIsInstance(self.reclamacion.cantidad_reclamada, float)

