from rest_framework import serializers
from ..models import User, Rol


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nombre', 'correo', 'telefono', 'activo', 'rol']