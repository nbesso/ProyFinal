from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cuenta/login/', login_request, name='login'),
    path('cuenta/logout/', LogoutView.as_view(template_name='AppLog/logout.html'), name='logout'),
    path('cuenta/register/', register, name='Register'),
    path('cuenta/editarPerfil/', editarPerfil, name='EditarPerfil'),
    #path('cuenta/avatar/', subir_avatar, name='SubirAvatar'),

]
