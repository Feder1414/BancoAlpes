from django.urls import path, include
from .views import  create_cliente, create_informacion_financiera
from .api import SolicitudViewSet, ClienteViewSet, InformacionFinancieraViewSet
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from .views import HealthCheck

router = DefaultRouter()
router.register('api/solicitudes', SolicitudViewSet, basename='solicitudes')
router.register('api/clientes', ClienteViewSet, basename='clientes')
router.register('api/informacionFinanciera', InformacionFinancieraViewSet, basename='informacionFinanciera')


urlpatterns = [
    path('crearCliente/', csrf_exempt(create_cliente), name='createCliente'),
    path('crearInformacionFinanciera/', csrf_exempt(create_informacion_financiera), name='createInformacionFinanciera'),
    path('health-check/', HealthCheck.as_view(), name='health-check'),
    path('', include(router.urls))

]