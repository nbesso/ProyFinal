from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.models import User
import django
from django.contrib.auth.decorators import login_required

# Create your views here.

#GON: Vista Login
def login_request(request):
    
    if request.method == 'POST':
        #Validación del formulario
        form = AuthenticationForm(request, data=request.POST)


        if form.is_valid():
            usuario = form.data.get('username')
            passwd = form.data.get('password')

            #Django valida usuario y contraseña.
            #Si el usuario es OK, crea cache y redirecciona.
            #Si el usuario está mal, redirecciona a la vista Login.
            user = authenticate(username=usuario, password=passwd)

            if user:
                login(request, user)

                return redirect('Inicio')
            else:
                return redirect('login')
                

        else:
            return redirect('login')
    
    form = AuthenticationForm()

    return render(request, 'AppLog/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            try:
                user_new = User.objects.get(username=username)
            except django.contrib.auth.models.User.DoesNotExist:
                user_new = None
            if not user_new:
                form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'AppLog/register.html', {'form': form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']        
            usuario.last_name = informacion['last_name']      
            usuario.first_name = informacion['first_name']  
            usuario.save()

            return render(request, 'blog/suscriptor_form.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, 'blog/editarPerfil.html', {'miFormulario':miFormulario,'usuario':usuario})

@login_required
def subir_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid:
            username = form.data['user']
            username.imagen = form['imagen']           
            username.save()
            return render(request,'blog/post_list.html')
    else:
        form=AvatarForm()

    return render(request, 'blog/agregar_avatar.html', {'form':form})
