from rest_framework import serializers
from ..models import Venta, User

class VentaSerializer(serializers.ModelSerializer):
    # Datos del usuario (lectura)
    usuario = serializers.CharField(source='usuario.nombre', read_only=True)

    class Meta:
        model = Venta
        fields = ['id', 'usuario', 'fecha', 'total', 'descripcion']