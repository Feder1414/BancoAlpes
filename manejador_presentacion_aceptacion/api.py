
from .models import Oferta, Solicitud, Cliente, InformacionFinanciera
from .serializers import OfertaSerializer, ClienteSerializer, SolicitudSerializer, InformacionFinancieraSerializer
import requests
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer



    def create(self,request,*args,**kwargs):
        cliente_id = request.data.get('pk')
        cliente = Cliente.objects.get(pk=cliente_id)
        solicitud = Solicitud.objects.create(cliente= cliente, estado = "nuevo")

        return Response(self.get_serializer(solicitud).data, status=status.HTTP_201_CREATED)



    @action(detail=False, methods=['post'], url_path='presentarOfertas')
    def presentarOfertas(self, request):
        
        solicitud_id = request.data.get('pk')
        solicitud = Solicitud.objects.get(pk = solicitud_id)
        if not hasattr(solicitud.cliente, 'informacionfinanciera'):
            return Response({"error": "El usuario de esta solicitud no tiene información financiera asociada, no se le pueden presentar las ofertas"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        informacionFinanciera = solicitud.cliente.informacionfinanciera
        if (informacionFinanciera.ingresos < informacionFinanciera.egresos):
            return Response({"error": "El usuario de esta solicitud no tiene los suficientes ingresos para cubrir sus egresos"}, status=status.HTTP_400_BAD_REQUEST)
        informacionFinancieraSerializada = InformacionFinancieraSerializer(informacionFinanciera)
        url = "http://127.0.0.1:8080/api/ofertas/generar-oferta/"

        response = requests.post(url, informacionFinancieraSerializada.data)
        
        print ("oasifuoiasd")
        if response.status_code == 201:
            ofertas = response.json()

            serializer = OfertaSerializer(data=ofertas)

            if serializer.is_valid():
                ofertas = serializer.save(solicitud = solicitud)
                solicitudP = Solicitud.objects.get(pk = solicitud_id)
                print(solicitudP.ofertas)
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            
            return Response("Mal D:", status=status.HTTP_400_BAD_REQUEST)



        



class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class InformacionFinancieraViewSet(viewsets.ModelViewSet):
    queryset = InformacionFinanciera.objects.all()
    serializer_class = InformacionFinancieraSerializer

    def create(self,request,*args,**kwargs):
        #En el json entra por parámetro pk que es el id del cliente
        cliente_id = request.data.get('pk')
        cliente = Cliente.objects.get(pk=cliente_id)
        if hasattr(cliente, 'informacionfinanciera'):
          return Response({"error": "Este usuario ya tiene información financiera asociada"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = InformacionFinancieraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cliente=cliente)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # informacionFinanciera = InformacionFinancieraSerializer(data=request.data).save()
        # cliente.informacionfinanciera = informacionFinanciera
        # cliente.save()
        # return Response(self.get_serializer(informacionFinanciera).data, status=status.HTTP_201_CREATED)
