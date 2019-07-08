from django.db import models
from django.contrib.auth.models import User

class Servicios(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Nombres = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=100)
    Ubicacion = models.CharField(max_length=200)
    ZipCode = models.CharField(max_length=100)
    Fecha = models.DateField(auto_now=False)
    # Hora = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.Nombres)

class Catalogo(models.Model):
    Nombre = models.CharField(max_length=100)
    Imagen = models.ImageField()
    Stock = models.IntegerField()

    def __str__(self):
        return "%s" % (self.Nombre)
