from django.db import models

# Create your models here. 
class Flor(models.Model):
    imagen = models.ImageField()
    nombre = models.CharField(max_length=80)
    valor = models.IntegerField()
    descripcion = models.TextField()
    estado = models.BooleanField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
