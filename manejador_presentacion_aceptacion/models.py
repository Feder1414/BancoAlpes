from django.db import models

class Tarjeta(models.Model):
    numero = models.CharField(max_length=16)
    fecha_vencimiento = models.DateField()
    cvv = models.CharField(max_length=3)
    fecha_aceptacion = models.DateField()
    hora_aceptacion = models.TimeField()
    oferta = models.ForeignKey('Oferta', on_delete=models.SET_NULL, null=True, blank=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.numero
    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'
        ordering = ['numero']

class Oferta(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=100)
    tasa = models.DecimalField(max_digits=5, decimal_places=2)
    franquicia = models.CharField(max_length=100)
    descripcion = models.TextField()
    solicitud = models.ForeignKey('Solicitud', on_delete=models.SET_NULL, null=True, blank=True, related_name = 'ofertas')

    def __str__(self):
        return str(self.tipo) + ' ' + self.monto
    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'
        ordering = ['monto']


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    #informacion_financiera = models.OneToOneField('InformacionFinanciera', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

class InformacionFinanciera(models.Model):
    ingresos = models.DecimalField(max_digits=10, decimal_places=2)
    egresos = models.DecimalField(max_digits=10, decimal_places=2)
    activos = models.DecimalField(max_digits=10, decimal_places=2)
    pasivos = models.DecimalField(max_digits=10, decimal_places=2)
    historial_crediticio = models.TextField(null = True, blank = True)
    puntuacion_crediticia = models.IntegerField(null = True, blank = True)
    antiguedad_laboral = models.IntegerField()
    tipo_empleo = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    numero_dependientes = models.IntegerField(default=0)
    historial_bancario = models.TextField(null=True, blank=True)
    garantias = models.TextField(null=True, blank=True)
    tipo_vivienda = models.CharField(max_length=100)
    educacion = models.CharField(max_length=100)
    cliente = models.OneToOneField('Cliente', on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.ingresos
    class Meta:
        verbose_name = 'InformacionFinanciera'
        verbose_name_plural = 'InformacionFinanciera'
        ordering = ['ingresos']

class Solicitud(models.Model):
    estado = models.CharField(max_length=100)
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True, blank=True, related_name= 'solicitudes')

