from django.urls import path, include
from .views import home, galeria, listado_flor, nueva_flor, modificar_flor, eliminar_flor, registro_usuario, FlorViewSet, guardar_token
from carrito.views import AgregarAlCarrito, EliminarDelCarrito
from rest_framework import routers

app_name='core'

router = routers.DefaultRouter()
router.register('flor', FlorViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('listado-flores/', listado_flor, name="listado_flores"),
    path('nueva-flores/', nueva_flor, name="nueva_flor"),
    path('modificar-flores/<id>/', modificar_flor, name="modificar_flor"),
    path('eliminar-flores/<id>/', eliminar_flor, name="eliminar_flor"),
    path('registro/', registro_usuario, name="registro_usuario"),
    path('carrito/<id>', AgregarAlCarrito, name='carrito'),
    path('remover/<id>', EliminarDelCarrito, name='remover_carrito'),
    path('galeria/carrito/<id>', AgregarAlCarrito, name='carrito'),
    path('galeria/remover/<id>', EliminarDelCarrito, name='remover_carrito'),
    path('api/', include (router.urls)),
    path('guardar-token/', guardar_token, name='guardar_token'),
] 