from django import forms ##Se importa el formulario base que trae dJango
from django.db.models import fields ##Se importa el tipo de datos de cada campo del formulario
from .models import Usuario ##Para la clase UsuarioForm se importan todos los metodos de Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    rut = forms.CharField(widget=forms.TextInput)
    #nombre = forms.CharField(widget=forms.TextInput)
    apellido = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField()
    edad = forms.IntegerField(widget=forms.TextInput)
    class Meta:
        model = User
        fields = ('rut','username','apellido','email','edad')


class UsuarioForm(forms.Form):
    class Meta:
        model = Usuario
        fields = ('rut','nombre','apellido','email','edad')