from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    nombre_producto = models.CharField(max_length=255)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_producto