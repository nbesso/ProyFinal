from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

# Importaciones desde Django
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'blog/Inicio.html')

#GON: Vista que muestra lista de Contactos creados
class SuscriptorList(ListView):
    model = Suscriptor
    template_name = "blog/suscriptor_list.html"

#GON: Vista que crea un Contacto y envía mensaje
class Suscribete(CreateView):
    model = Suscriptor
    success_url = "/blog/inicio/#suscribite"
    fields = ['nombre', 'apellido', 'email']

#GON: Vista para visualizar Detalles de un Contacto ya creado.
class Detalle_suscriptor(DetailView):
    model = Suscriptor
    template_name = "blog/suscriptor_detalle.html"

#GON: Vista que modifica un Contacto.
class Modifica_suscriptor(UpdateView):
    model = Suscriptor
    success_url = "/blog/editar/<int:pk>/"
    fields = ['nombre', 'apellido', 'email']

#GON: Vista que elimina un Contacto.
class Elimina_suscriptor(DeleteView):
    model = Suscriptor
    success_url = "/blog/suscriptor/list"


#FACU: Vista que lista post.

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    queryset = Post.objects.filter(status=1).order_by('-creado_el')

class PostListSelf(ListView):
    model = Post
    template_name = 'blog/post_list_self.html'
    queryset = Post.objects.filter(status=1).order_by('-creado_el')

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detalle.html'

class PostCreate(CreateView):
    model = Post
    success_url = "/blog/post/list"
    fields = ['titulo','autor','status','contenido','slug']

class PostUpdate(UpdateView):
    model = Post
    success_url = "/blog/post/list"
    fields = ['titulo','status','contenido']

class PostDelete(DeleteView):
    model = Post
    success_url = "/blog/post/list"

def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})    