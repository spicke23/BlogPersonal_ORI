from django import forms ##Se importa el formulario base que trae dJango
from django.db.models import fields ##Se importa el tipo de datos de cada campo del formulario
from .models import Usuario ##Para la clase UsuarioForm se importan todos los metodos de Usuario

class RegistroForm(forms.Form):
    rut = forms.CharField(widget=forms.TextInput)
    nombre = forms.CharField(widget=forms.TextInput)
    apellido = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginFormUsuario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

#class UsuarioForm(forms.Form):
#    class Meta:
#        model = Usuario
#        fields = ('rut','nombre','apellido','email','edad')

