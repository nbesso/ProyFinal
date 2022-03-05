from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Info_adicional(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Agregamos la imagen del Avatar
    imagen = models.ImageField(upload_to='avatares', null=True, blank= True)
