from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from .models import Avatar
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name')


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Reingrese Contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    avatar = forms.ImageField(label="Carga aqui tu Avatar")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name', 'avatar']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']