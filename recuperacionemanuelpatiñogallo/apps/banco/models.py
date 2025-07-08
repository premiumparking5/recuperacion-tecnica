from django.db import models
class Banco(models.Model):
    credito = models.TextField("credito")
    debito = models.TextField("debito")
