# Generated by Django 4.2.2 on 2023-06-25 07:59

from django.db import migrations, models
import api.reclamaciones.models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamaciones', '0002_rename_arrival_airport_reclamacion_aeropuerto_llegada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamacion',
            name='numero_vuelo',
            field=models.CharField(default='AB1234', max_length=6, validators=[api.reclamaciones.models.validate_flight_number], verbose_name='Número de vuelo'),
        ),
    ]
