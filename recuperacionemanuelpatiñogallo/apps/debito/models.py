from django.db import models
class debito(models.Model):
   gasto = models.TextField("gasto")
   banco = models.TextField("banco")

