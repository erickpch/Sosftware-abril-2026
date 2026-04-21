from rest_framework import viewsets
from ..models import Venta
from ..serializers import VentaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    
    
    # POST /ventas/getFecha/
    @action(detail=False, methods=['post'], url_path='getFecha')
    def getFecha(self, request):
        fecha = request.data.get("fecha")

        if not fecha:
            return Response(
                {"error": "Debe enviar el campo 'fecha' en formato YYYY-MM-DD"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Convertir fecha a objeto datetime
            from datetime import datetime
            fecha_dt = datetime.fromisoformat(fecha)
        except:
            return Response(
                {"error": "Formato de fecha inválido. Use YYYY-MM-DD"},
                status=status.HTTP_400_BAD_REQUEST
            )

        ventas = Venta.objects.filter(fecha__gt=fecha_dt)
        serializer = VentaSerializer(ventas, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)