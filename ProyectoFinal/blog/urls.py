from django.urls import path
from blog.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
]