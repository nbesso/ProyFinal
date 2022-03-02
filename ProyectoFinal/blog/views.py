from django.shortcuts import render

# Importaciones desde Django
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'blog/contacto_form.html')


#GON: Vista que muestra lista de Contactos creados
class ContactoList(ListView):
    model = Contacto
    template_name = "blog/contacto_list.html"

#GON: Vista que crea un Contacto y envía mensaje
class Contactanos(CreateView):
    model = Contacto
    success_url = "/blog/contacto/list"
    fields = ['nombre', 'apellido', 'email' , 'telefono', 'mensaje']

#GON: Vista para visualizar Detalles de un Contacto ya creado.
class Detalle_contacto(DetailView):
    model = Contacto
    template_name = "blog/contacto_detalle.html"

#GON: Vista que modifica un Contacto.
class Modifica_contacto(UpdateView):
    model = Contacto
    success_url = "/blog/contacto/list"
    fields = ['nombre', 'apellido', 'email' , 'telefono', 'mensaje']

#GON: Vista que elimina un Contacto.
class Elimina_contacto(DeleteView):
    model = Contacto
    success_url = "/blog/contacto/list"
