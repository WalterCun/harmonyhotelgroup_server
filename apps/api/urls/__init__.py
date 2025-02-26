from .hotel_url import urlpatterns as hotel_url
from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.api.urls.hotel_url')),
    path('v1/', include('apps.api.urls.all_url')),
    path('v1/', include('apps.api.urls.metrics_url')),
    path('v1/', include('apps.api.urls.offer_url')),
    path('v1/', include('apps.api.urls.prospect_url')),
    path('v1/', include('apps.api.urls.social_network_url')),
    path('v1/', include('apps.api.urls.tours_url')),
]
