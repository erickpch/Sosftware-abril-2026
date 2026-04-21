from django.db import models
from miApp.models import Rol

class User(models.Model):
    nombre = models.CharField(max_length= 30)
    correo = models.EmailField(unique = True)
    telefono = models.PositiveIntegerField()
    activo = models.BooleanField()

    rol = models.ForeignKey(Rol, on_delete = models.CASCADE)