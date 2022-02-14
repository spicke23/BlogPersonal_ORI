from django import views
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
    path('login', views.login),
    path('bienvenido', views.bienvenido),
    path('logout', views.salir),
    path('showuserlist', views.listadoUsuarios),
]