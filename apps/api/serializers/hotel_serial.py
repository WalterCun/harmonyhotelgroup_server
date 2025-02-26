from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.api.models import Hotel, Location, Service
from apps.core.models import City


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'description', 'is_active']


class CitySerializer(ModelSerializer):
    province = CharField(source='province.name')
    country = CharField(source='province.country.name')

    class Meta:
        model = City
        fields = ['name', 'province', 'country']


class LocationSerializer(ModelSerializer):
    city = CharField(source='city.name')
    province = CharField(source='city.province.name')
    country = CharField(source='city.province.country.name')

    class Meta:
        model = Location
        fields = [
            "city",
            "province",
            "country",
            "main_street",
            "house_number",
            "intersection",
            "latitude",
            "longitude",
            "map_url",
            "is_active",
        ]


class HotelSerializer(ModelSerializer):
    location = LocationSerializer()
    services = SerializerMethodField()

    class Meta:
        model = Hotel
        exclude = ['created_at', 'updated_at']

    @staticmethod
    def get_services(instance):
        """
        Filtrar informacion de servicios activos.
        """
        active_services = instance.services.filter(is_active=True)
        return ServiceSerializer(active_services, many=True).data
