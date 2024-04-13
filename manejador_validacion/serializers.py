from rest_framework import serializers
from .models import Transaccion

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = ('id',
                  'cuenta_origen', 
                  'titular_origen',
                  'cuenta_destino',
                  'titular_destino',
                  'monto',
                  'dateTime'
                )
        