from rest_framework.serializers import ModelSerializer

from apps.api.models import OfferTag, Offer
from apps.api.serializers.hotel_serial import HotelSerializer


class OfferTagsSerializer(ModelSerializer):
    class Meta:
        model = OfferTag
        fields = '__all__'


class OfferSerializer(ModelSerializer):
    hotel = HotelSerializer

    class Meta:
        model = Offer
        fields = '__all__'
