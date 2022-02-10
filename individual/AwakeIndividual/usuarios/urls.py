from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registro/',views.registro),
    path('recibir/',views.recibir),
    path('sumar/<int:numero1>/<int:numero2>/',views.sumar),
    path('usuarios', views.usuarios),
    path('procesarFormularioUsuario', views.procesarRegistro),
    path('procesarRegistroForm', views.procesarRegistroForm),
]