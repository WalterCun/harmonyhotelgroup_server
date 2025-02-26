from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.models import Hotel
from apps.api.serializers.hotel_serial import HotelSerializer


class HotelListView(APIView):
    """
    Vista para manejar la lista de hoteles.
    Devuelve todos los hoteles o filtra por nombre y/o ciudad si son proporcionados.
    """
    serializer_class = HotelSerializer  # Definimos explícitamente el serializador

    def get(self, request, *args, **kwargs):
        # Recuperamos los parámetros de la consulta
        nombre = request.query_params.get('nombre')  # /api/hoteles/?nombre=Hotel1
        ciudad = request.query_params.get('ciudad')  # /api/hoteles/?ciudad=Paris

        # Base queryset: todos los hoteles
        queryset = Hotel.objects.filter(is_active=True,
                                        location__is_active=True,
                                        location__city__is_active=True,
                                        location__city__province__is_active=True,
                                        location__city__province__country__is_active=True,
                                        ).order_by('name')

        # Si no hay resultados y se aplicaron filtros, devolvemos error 404
        if not queryset.exists():
            raise NotFound("No se encontraron informacion de hoteles.")

        # Filtramos si hay parámetros proporcionados
        if nombre:
            queryset = queryset.filter(name__icontains=nombre)  # Coincidencia parcial en el nombre
        if ciudad:
            queryset = queryset.filter(city__icontains=ciudad)  # Coincidencia parcial en la ciudad

        # Serializamos los resultados y los devolvemos
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
