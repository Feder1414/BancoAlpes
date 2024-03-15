from django.shortcuts import render
from .forms import ClienteForm, InformacionFinancieraForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logica_cliente import crear_cliente
from .logic.logica_informacion_financiera import crear_informacion_financiera
from .models import Oferta, Solicitud, Cliente
from .serializers import OfertaSerializer, ClienteSerializer, SolicitudSerializer
import requests
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


# def cliente_list(request):
#     measurements = get_measurements()
#     context = {
#         'measurement_list': measurements
#     }
#     return render(request, 'Measurement/measurements.html', context)

def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            crear_cliente(form)
            messages.add_message(request, messages.SUCCESS, 'create cliente successful')
            return HttpResponseRedirect(reverse('createCliente'))
        else:
            print(form.errors)
    else:
        form = ClienteForm()

    context = {
        'form': form,
    }

    return render(request, 'Cliente/crearCliente.html', context)

def create_informacion_financiera(request):
    if request.method == 'POST':
        form = InformacionFinancieraForm(request.POST)
        if form.is_valid():
            crear_informacion_financiera(form)
            messages.add_message(request, messages.SUCCESS, 'create informacion financiera successful')
            return HttpResponseRedirect(reverse('createInformacionFinanciera'))
        else:
            print(form.errors)
    else:
        form = InformacionFinancieraForm()

    context = {
        'form': form,
    }

    return render(request, 'InformacionFinanciera/crearInformacionFinanciera.html', context)









        
        


    


# def presentarOfertas(request,pk):
#     ofertasManejadorViabilidad = requests.get(url = "nkmsdnsdfl")
#     #Vuleve el json un diccionario
#     ofertas = ofertasManejadorViabilidad.json()
#     #
#     for oferta in ofertas["ofertas"]:
#         ofertaM=crear_oferta(oferta)
#         tarjetaM = crear_tarjeta(oferta["tarjeta"])
#         tarjetaM.oferta = ofertaM
#         tarjetaM.save()

#     return ofertas

        






    pass







