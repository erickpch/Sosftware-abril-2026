from rest_framework import serializers
from ..models import User, Rol

class UserSerializer(serializers.ModelSerializer):
    # Mostrar info del rol (lectura)
    rol = serializers.CharField(source='rol.nombre', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'nombre', 'correo', 'telefono', 'activo', 'rol']