from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(max_length=10, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50)
    edad = models.IntegerField()