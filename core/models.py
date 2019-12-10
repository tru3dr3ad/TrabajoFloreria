from django.db import models

# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre
    

class Flor(models.Model):
    imagen = models.ImageField()
    nombre = models.CharField(max_length=80)
    valor = models.IntegerField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estado = models.BooleanField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
