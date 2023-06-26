from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from api.clientes.models import Cliente

# ------------------- Tests para el modelo Cliente -------------------

class ClienteTests(APITestCase):
    """Probamos que se puede crear un cliente correctamente."""

    def setUp(self):
        # primero creamos un usuario de Django, solo admin puede crear clientes
        self.user = User.objects.create_superuser(
            username="test",
            password="test"
        )
        # creamos el gupo cliente para que se pueda asignar al usuario que se va a crear,
        # no confundir con el usuario que crea el cliente, que es un admin.
        grupo_cliente = Group.objects.create(name='cliente')
        # luego objener el token para el usuario
        self.token, created = Token.objects.get_or_create(user=self.user)

    def test_nuevo_cliente(self):
       # Nos aseguramos de que se puede crear un nuevo cliente.
        url =  reverse('cliente-create')
        data = {'nombre': 'Test',
                'apellidos': 'Test',
                'email': 'test@test.com',
                'telefono': '+34 123456789'}
        
        # Simulate authentication for the user
        self.client.force_authenticate(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(self.user.is_authenticated, True)
        self.assertEqual(self.user.is_superuser, True)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Cliente.objects.get().nombre, 'Test')

class ClienteNoAutenticadoTests(APITestCase):
    """
    Probamos que no se puede crear un cliente si no se está autenticado.
    """
    def test_no_se_puede_crear_nuevo_cliente(self):
        """
        Nos aseguramos de que un usuario no autenticado no puede crear un nuevo cliente.
        """
        url =  reverse('cliente-create')
        data = {'nombre': 'Test',
                'apellidos': 'Test',
                'email': 'test@test.com',
                'telefono': '+34 123456789'}
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ClienteNoAdminTest(APITestCase):
    """
    Probamos que no se puede crear un cliente si no se es admin.
    """
    def setUp(self):
        # primero creamos un usuario de Django, solo admin puede crear clientes
        self.user = User.objects.create_user(
            username="test",
            password="test"
        )
        grupo_cliente = Group.objects.create(name='cliente')
        grupo_cliente.user_set.add(self.user)
        # luego objener el token para el usuario
        self.token, created = Token.objects.get_or_create(user=self.user)

    def test_solo_admin_puede_crear_nuevo_cliente(self):
        """
        Nos aseguramos de que un usuario no admin no puede crear un nuevo cliente.
        """
        url =  reverse('cliente-create')
        data = {'nombre': 'Test',
                'apellidos': 'Test',
                'email': 'test@test.com',
                'telefono': '+34 123456789'}

        # Simulate authentication for the user
        self.client.force_authenticate(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(self.user.is_authenticated, True)
        self.assertEqual(self.user.is_superuser, False) # no es admin

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

# ------------------- Tests para el modelo Reclamación -------------------

class ReclamacionTests(APITestCase):
    """Pronamos que se puede crear una reclamación correctamente."""
    def setUp(self):

        # primero creamos un usuario de Django
        self.user = User.objects.create_user(
            username="test",
            password="test"
        )
        # luego creamos el grupo cliente y lo asignamos al usuario
        grupo_cliente = Group.objects.create(name='cliente')
        grupo_cliente.user_set.add(self.user)
        # luego objener el token para el usuario
        self.token, created = Token.objects.get_or_create(user=self.user)

        # luego creamos un cliente
        self.cliente = Cliente.objects.create(
            user=self.user,
            nombre="Test",
            apellidos="Test",
            email="test@test.com",
            telefono="+34 123456789")
    
    def test_nueva_reclamacion(self):
        # Nos aseguramos de que se puede crear una nueva reclamación.
        url =  reverse('reclamacion-create')
        data = {'cliente': self.cliente.id,
                'fecha_vuelo': '2020-12-12',
                'numero_vuelo': 'IB1234',
                'nombre_aerolinea': 'Iberia',
                'aeropuerto_salida': 'ABC',
                'aeropuerto_llegada': 'ABC'}
        
        # Simulate authentication for the user
        self.client.force_authenticate(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.assertEqual(self.user.is_authenticated, True)
        self.assertEqual(self.user.is_superuser, False) # no es admin
        # comprobamos que el usuario tiene el grupo cliente
        self.assertEqual(self.user.groups.filter(name='cliente').exists(), True)

        # hacemos la petición
        response = self.client.post(url, data, format='json')
        # comprobamos que se ha creado correctamente
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReclamacionNoAdminTests(APITestCase):
    pass
