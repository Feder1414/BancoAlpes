# Generated by Django 5.0.3 on 2024-03-15 00:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionFinanciera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingresos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('egresos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pasivos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('historial_crediticio', models.TextField(blank=True, null=True)),
                ('puntuacion_crediticia', models.IntegerField(blank=True, null=True)),
                ('antiguedad_laboral', models.IntegerField()),
                ('tipo_empleo', models.CharField(max_length=100)),
                ('estado_civil', models.CharField(max_length=50)),
                ('numero_dependientes', models.IntegerField(default=0)),
                ('historial_bancario', models.TextField(blank=True, null=True)),
                ('garantias', models.TextField(blank=True, null=True)),
                ('tipo_vivienda', models.CharField(max_length=100)),
                ('educacion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'InformacionFinanciera',
                'verbose_name_plural': 'InformacionFinanciera',
                'ordering': ['ingresos'],
            },
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tasa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('franquicia', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
                'ordering': ['monto'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('pais', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('informacion_financiera', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manejador_presentacion_aceptacion.informacionfinanciera')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=16)),
                ('fecha_vencimiento', models.DateField()),
                ('cvv', models.CharField(max_length=3)),
                ('fecha_aceptacion', models.DateField()),
                ('hora_aceptacion', models.TimeField()),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manejador_presentacion_aceptacion.cliente')),
                ('oferta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manejador_presentacion_aceptacion.oferta')),
            ],
            options={
                'verbose_name': 'Tarjeta',
                'verbose_name_plural': 'Tarjetas',
                'ordering': ['numero'],
            },
        ),
    ]