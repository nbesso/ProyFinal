from django.urls import path
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('inicio/', Suscribete.as_view(), name='Inicio'),
    path('suscriptor/list', SuscriptorList.as_view(), name = 'List'),
    path('<int:pk>/', Detalle_suscriptor.as_view(), name='Detail'),
    path('editar/<int:pk>/', Modifica_suscriptor.as_view(), name='Edit'),
    path('borrar/<int:pk>/', Elimina_suscriptor.as_view(), name='Delete'),
    path('post/create', PostCreate.as_view(), name='post_create'),
    path('post/update/<slug:slug>/', PostUpdate.as_view(), name='post_update'),
    path('post/delete/<slug:slug>/', PostDelete.as_view(), name='post_delete'),
    path('post/list', PostList.as_view(), name='post_list'),
    path('post/list/self', PostListSelf.as_view(), name='post_list_self'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    
]

