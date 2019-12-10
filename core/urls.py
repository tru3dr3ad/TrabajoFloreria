from django.urls import path
from .views import home, galeria, listado_flor, nueva_flor, modificar_flor, eliminar_flor, registro_usuario

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('listado-flores/', listado_flor, name="listado_flores"),
    path('nueva-flores/', nueva_flor, name="nueva_flor"),
    path('modificar-flores/<id>/', modificar_flor, name="modificar_flor"),
    path('eliminar-flores/<id>/', eliminar_flor, name="eliminar_flor"),
    path('registro/', registro_usuario, name="registro_usuario"),
]