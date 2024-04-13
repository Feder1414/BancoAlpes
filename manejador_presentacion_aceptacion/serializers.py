from rest_framework import serializers
from . models import Oferta, Solicitud, Tarjeta,Cliente, InformacionFinanciera

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ['numero', 'fecha_vencimiento', 'cvv', 'fecha_aceptacion', 'hora_aceptacion']


class OfertaSerializer(serializers.ModelSerializer):
    tarjeta = TarjetaSerializer(read_only=True)
    class Meta:
        model = Oferta
        fields = ['monto', 'tipo', 'tasa', 'franquicia', 'descripcion', 'tarjeta']
        



class SolicitudSerializer(serializers.ModelSerializer):
    ofertas = OfertaSerializer(many=True, read_only=True)
    class Meta:
        model = Solicitud
        fields = ['estado', 'ofertas']





class InformacionFinancieraSerializer(serializers.ModelSerializer):
    #cliente = ClienteSerializer(read_only=True)
    class Meta:
        model = InformacionFinanciera
        fields = [
            'ingresos', 
            'egresos', 
            'activos', 
            'pasivos', 
            'historial_crediticio', 
            'puntuacion_crediticia', 
            'antiguedad_laboral', 
            'tipo_empleo', 
            'estado_civil', 
            'numero_dependientes', 
            'historial_bancario', 
            'garantias', 
            'tipo_vivienda', 
            'educacion', 
        ]

class ClienteSerializer(serializers.ModelSerializer):
    solicitudes = SolicitudSerializer(many=True, read_only=True)
    tarjetas = TarjetaSerializer(many=True, read_only=True)
    informacionfinanciera = InformacionFinancieraSerializer(read_only=True) 


    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'direccion', 'ciudad', 'departamento', 'codigo_postal', 'pais', 'telefono', 'email', 'fecha_nacimiento', 'solicitudes', 'tarjetas', 'informacionfinanciera']