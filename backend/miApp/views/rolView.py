from rest_framework import viewsets
from ..models import Rol
from ..serializers import RolSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

    @action(detail = False, methods = ['get'], url_path = 'hola')
    def saludo(self, resquest):
        saludo = "hola a todos"        
        return Response(saludo)
    
    @action(detail = False, methods = ['post'], url_path = 'evento')
    def disparador(self, request):

        mensaje =  request.data.get("mensaje","mensaje vacio")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notificacion",
            {
                "type": "evento",
                "data": mensaje
            }
        )

        return Response ({ "mensaje": "socket enviado"})
        


