from django.db import models
from django.contrib.auth import get_user_model
from core.models import Flor

# Create your models here.
Usuario = get_user_model()

# Modelo del carrito
class Carrito(models.Model):
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    item = models.ForeignKey(Flor, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} of {self.item.nombre}'
    
class Pedido(models.Model):
    itemsPedido = models.ManyToManyField(Carrito)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ordenado = models.BooleanField(default=False)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username
    