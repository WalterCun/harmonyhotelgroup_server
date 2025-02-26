from rest_framework.serializers import ModelSerializer

from apps.api.models.tours_model import TourCategory, PriceType, TourVideo, TourImage
from apps.api.serializers.hotel_serial import HotelSerializer


class TourCategorySerializer(ModelSerializer):
    class Meta:
        model = TourCategory
        fields = '__all__'


class PriceTypeSerializer(ModelSerializer):
    class Meta:
        model = PriceType
        fields = '__all__'


class TourDestinationSerializer(ModelSerializer):
    hotels = HotelSerializer
    price_type = PriceTypeSerializer
    category = TourCategorySerializer

    class Meta:
        model = TourCategory
        fields = '__all__'


class TourImageSerializer(ModelSerializer):
    tour = TourDestinationSerializer

    class Meta:
        model = TourImage
        fields = '__all__'


class TourVideoSerializer(ModelSerializer):
    tour = TourDestinationSerializer

    class Meta:
        model = TourVideo
        fields = '__all__'
