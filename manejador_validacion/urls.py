from django.urls import path, include
from rest_framework import routers
from .api import TransaccionViewSet
from .views import TransferListAPIView

router = routers.DefaultRouter()
router.register('api/transacciones', TransaccionViewSet, basename='transacciones')

urlpatterns = urlpatterns = [
    path('api/transacciones/titular/<int:owner_id>/', TransferListAPIView.as_view(), name='transfer-list'),
    path('', include(router.urls))

]