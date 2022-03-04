from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name')

        