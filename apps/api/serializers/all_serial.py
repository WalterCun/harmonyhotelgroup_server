from rest_framework.serializers import Serializer

from apps.api.serializers.hotel_serial import HotelSerializer
from apps.api.serializers.offer_serial import OfferSerializer
from apps.api.serializers.tours_serial import TourDestinationSerializer


class AllSerializer(Serializer):
    featuredHotels = HotelSerializer(many=True,required=False)
    nearbyDestinations = TourDestinationSerializer(many=True,required=False)
    specialOffers = OfferSerializer(many=True,required=False)

    class Meta:
        fields = ['featuredHotels', 'nearbyDestinations', 'specialOffers']
