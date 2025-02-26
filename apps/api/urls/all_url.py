from django.urls import path

from apps.api.views import AllView

urlpatterns = [
    path('global', AllView.as_view(), name='all'),
]