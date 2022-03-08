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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)