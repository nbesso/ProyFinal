from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
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

            return redirect('Login')

    else:
        form = UserRegisterForm()

    return render(request, 'AppLog/register.html', {'form': form})