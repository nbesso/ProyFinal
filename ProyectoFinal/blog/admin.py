from django.contrib import admin
from blog.models import *

# Register your models here.

class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','email')
    list_filter = ('email',)
    search_fields = ['apellido']

admin.site.register(Suscriptor, SuscriptorAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'status','creado_el','autor')
    list_filter = ("status",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    #como auto completar el usuario?

admin.site.register(Post, PostAdmin)