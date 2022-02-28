from django.urls import path
from blog.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('contacto/list', ContactoList.as_view(), name = 'List'),
    path('nuevo/', Creacion_contacto.as_view(), name='New'),
    path('<int:pk>/', Detalle_contacto.as_view(), name='Detail'),
    path('editar/<int:pk>/', Modifica_contacto.as_view(), name='Edit'),
    path('borrar/<int:pk>/', Elimina_contacto.as_view(), name='Delete'),
]