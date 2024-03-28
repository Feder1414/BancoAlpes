# Generated by Django 5.0.1 on 2024-03-15 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manejador_presentacion_aceptacion', '0004_solicitud_oferta_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='solicitudes', to='manejador_presentacion_aceptacion.cliente'),
        ),
    ]