from rest_framework.serializers import ModelSerializer

from apps.api.models.social_network import SocialNetwork, SocialPlatform
from apps.api.serializers.hotel_serial import HotelSerializer


class SocialPlatformSerializer(ModelSerializer):
    class Meta:
        model = SocialPlatform
        fields = '__all__'


class SocialNetworkSerializer(ModelSerializer):
    hotel = HotelSerializer
    platform = SocialPlatformSerializer

    class Meta:
        model = SocialNetwork
        fields = '__all__'
