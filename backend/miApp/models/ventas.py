from django.db import models
from miApp.models import *


class Venta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ventas")
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Venta #{self.id} - {self.usuario.username} - ${self.total}"