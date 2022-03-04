from django.urls import path
from blog.views import *

urlpatterns = [
    path('inicio/', Suscribete.as_view(), name='Inicio'),
    path('suscriptor/list', SuscriptorList.as_view(), name = 'List'),
#    path('nuevo/', Creacion_contacto.as_view(), name='New'),
    path('<int:pk>/', Detalle_suscriptor.as_view(), name='Detail'),
    path('editar/<int:pk>/', Modifica_suscriptor.as_view(), name='Edit'),
    path('borrar/<int:pk>/', Elimina_suscriptor.as_view(), name='Delete'),
]