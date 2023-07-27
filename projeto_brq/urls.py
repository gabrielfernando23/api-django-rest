from django.contrib import admin
from django.urls import path, include
from brq.views import ClientesViewSet, TiposDeTransacaoViewSet, TransacoesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('tipos-de-transacao', TiposDeTransacaoViewSet, basename='Tipos_De_Transacao')
router.register(r'transacoes', TransacoesViewSet, basename='Transacao')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
