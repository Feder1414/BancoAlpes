from django.db import models

from manejador_presentacion_aceptacion.models import Cliente

class Transaccion(models.Model):
    cuenta_origen = models.CharField(max_length=16)
    titular_origen = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
    cuenta_destino = models.CharField(max_length=16)
    titular_destino = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    dateTime = models.DateTimeField()

    def __str__(self) -> str:
        return 'titular origen = %s; titular destino = %s' % (self.titular_origen, self.titular_destino) 
