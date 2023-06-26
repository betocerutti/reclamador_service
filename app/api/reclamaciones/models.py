from datetime import datetime
import re

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from api.clientes.models import Cliente


def validate_airport_code(code):
    pattern = r'^[A-Z]{3}$'
    if not re.match(pattern, code):
        raise ValidationError("Código de aeropuerto no válido.")
    return True

def validate_flight_number(flight_number):
    pattern = r'^[A-Za-z]{2}\d{4}$'
    if not re.match(pattern, flight_number):
        raise ValidationError("Código de vuelo no válido.")


class Reclamacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_vuelo = models.DateTimeField(verbose_name="Fecha del vuelo")
    numero_vuelo = models.CharField(max_length=6, verbose_name="Número de vuelo", default="AB1234", validators=[validate_flight_number])
    nombre_aerolinea = models.CharField(max_length=100, verbose_name="Nombre de la aerolínea", default="undefined")
    aeropuerto_llegada = models.CharField(max_length=3, verbose_name="Aeropuerto de llegada", default="000", validators=[validate_airport_code])
    aeropuerto_salida = models.CharField(max_length=3, verbose_name="Aeropuerto de salida", default="000", validators=[validate_airport_code])
    
    fecha_vista = models.DateTimeField(verbose_name="Fecha vista", null=True, blank=True)
    numero_expediente = models.CharField(max_length=100, verbose_name="Número de expediente", null=True, blank=True)
    cantidad_reclamada = models.FloatField(verbose_name="Cantidad reclamada", null=True, blank=True)

    class Meta:
        verbose_name = 'Reclamacion'
        verbose_name_plural = 'Reclamaciones'

    def __str__(self):
        return "Reclamación de {} para el vuelo {} de {}".format(
            self.cliente.email, self.numero_vuelo, self.fecha_vuelo)
    
    def get_absolute_url(self):
        # por simplicidad se hace de esta manera, deberia de ir con url.reverse
        return "/reclamaciones/" + str(self.id) + "/"
    

    def inicializar(self):
        """
        Inicializa la reclamación, registrándola en la base de datos y
        y envía un correo electrónico al cliente con el número de expediente.
        
        Sugerencia: este sería un sitio donde usar Celery para enviar el correo
        electrónico en segundo plano, ya que puede tardar un poco.

        Por ahora, vamos a simular que se ha registrado correctamente
        inicializando los campos relevantes y devolviendo True.
        
        """
        
        self.fecha_vista = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
        self.numero_expediente = "123456789"
        self.cantidad_reclamada = 250.00
        self.save()

        return True
    