from logging import PlaceHolder
from pydoc import text
from django.db import models

# Create your models here.


#GON: Modelo para crear un contacto y enviar un mesaje

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    apellido = models.CharField(max_length=40, null=False)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return f'Datos de Suscriptor: {self.nombre} {self.apellido}'
        