from django.db.models import Q
from rest_framework import generics
from .models import Transaccion
from .serializers import TransaccionSerializer

class TransferListAPIView(generics.ListAPIView):
    serializer_class = TransaccionSerializer

    def get_queryset(self):
        owner_id = self.kwargs['owner_id']  
        #retornmaos las transacciones que tengan titular de origen o destino igual al del cliente que buscamos
        return Transaccion.objects.filter(Q(titular_origen=owner_id) | Q(titular_destino=owner_id))
