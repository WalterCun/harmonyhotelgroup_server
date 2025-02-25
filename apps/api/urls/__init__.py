from .hotel_url import urlpatterns as hotel_url
from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.api.urls.hotel_url')),
    # path('v1/', include(hotel_url)),
]