from django.db import models

# Create your models here.


#GON: Modelo para crear un contacto y enviar un mesaje

class Contacto(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    apellido = models.CharField(max_length=40, null=False)
    email = models.EmailField(unique=True, null=False)
    telefono = models.IntegerField(unique=True, null=False)
    mensaje = models.CharField(max_length=250, null=False)

