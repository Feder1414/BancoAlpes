from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('crearCliente/', csrf_exempt(views.create_cliente), name='createCliente'),
    path('crearInformacionFinanciera/', csrf_exempt(views.create_informacion_financiera), name='createInformacionFinanciera'),
    path('presentarOfertas/<int:idSolicitud>/', csrf_exempt(views.create_cliente), name='createCliente')

]