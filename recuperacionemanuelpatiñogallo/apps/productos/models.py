from django.db import models


class Producto(models.Model):
    nombre = models.TextField("nombre")
    precio = models.IntegerField("precio")
    