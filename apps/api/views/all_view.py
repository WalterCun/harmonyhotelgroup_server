from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.models import Hotel, Offer, TourDestination
from apps.api.serializers.all_serial import AllSerializer



class AllView(APIView):
    serializer_class = AllSerializer

    def get(self, request, *args, **kwargs):
        queryset_hotel = Hotel.objects.filter(is_active=True)[:2]
        queryset_tours = TourDestination.objects.filter(is_active=True)[:5]
        queryset_offers = Offer.objects.filter(is_active=True, end_date__gte=now())[:3]

        data_instance = {
            'featuredHotels': list(queryset_hotel),
            'nearbyDestinations': list(queryset_tours),
            'specialOffers': list(queryset_offers)
        }

        # Pasamos los datos como instancia para que se serialicen
        serializer = self.serializer_class(instance=data_instance)
        return Response(serializer.data)
