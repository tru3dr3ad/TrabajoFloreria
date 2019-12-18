from django.contrib import admin
from core.models import Flor
from carrito.models import Carrito, Pedido
# Register your models here.

class FlorAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','valor','descripcion', 'estado', 'stock']
    search_fields = ['nombre', 'valor']
    list_filter = ['estado']
    list_per_page = 15

admin.site.register(Flor, FlorAdmin)
admin.site.register(Carrito)
admin.site.register(Pedido)