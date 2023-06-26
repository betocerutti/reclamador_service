from rest_framework import serializers

from .models import Reclamacion


class ReclamacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reclamacion
        fields = '__all__'

    def save(self, **kwargs):

        reclamacion = Reclamacion(
            cliente=self.validated_data['cliente'],
            fecha_vuelo=self.validated_data['fecha_vuelo'],
            numero_vuelo=self.validated_data['numero_vuelo'],
            nombre_aerolinea=self.validated_data['nombre_aerolinea'],
            aeropuerto_salida=self.validated_data['aeropuerto_salida'],
            aeropuerto_llegada=self.validated_data['aeropuerto_llegada'],
        )

        reclamacion.save()
        reclamacion.inicializar()

        return reclamacion