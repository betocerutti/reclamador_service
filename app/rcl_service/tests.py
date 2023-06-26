from django.test import TestCase
from django.contrib.auth.models import User
import requests


class APIOnlineTestCase(TestCase):

    def test_api_online(self):
        response = requests.get('http://localhost:8000/api/v1/clientes/')
        self.assertEqual(response.status_code, 403)


