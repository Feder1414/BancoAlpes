from rest_framework import serializers
from .models import Transaccion
from manejador_presentacion_aceptacion.serializers import ClienteSerializer

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = (
                  'cuenta_origen', 
                  'titular_origen',
                  'cuenta_destino',
                  'titular_destino',
                  'monto',
                  'dateTime'
        )
        