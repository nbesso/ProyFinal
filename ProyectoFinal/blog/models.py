from logging import PlaceHolder
from pydoc import text
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.


#GON: Modelo para crear un contacto y enviar un mesaje

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    apellido = models.CharField(max_length=40, null=False)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return f'Datos de Suscriptor: {self.nombre} {self.apellido}'
        
# FACU: Modelo para crear un blog

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    modificado_el = models.DateTimeField(auto_now= True)
    contenido = RichTextUploadingField()
    creado_el = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-creado_el']

    def __str__(self):
        return self.titulo
