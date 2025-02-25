from django.urls import path

from apps.api.views.hotel_view import HotelListView

urlpatterns = [
    path('hoteles', HotelListView.as_view(), name='hotel-list'),
]
