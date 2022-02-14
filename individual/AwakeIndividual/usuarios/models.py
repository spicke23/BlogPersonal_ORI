from django import forms
from django.db.models import fields

# Create your models here.
class Usuario(forms.Form):
    rut = forms.CharField(widget=forms.TextInput)
    nombre = forms.CharField(widget=forms.TextInput)
    apellido = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginFormUsuario(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

#codefirst
#class Producto(models.Model):
#    nombre = models.CharField(max_length=50, null=False)
#    precio = models.IntegerField()