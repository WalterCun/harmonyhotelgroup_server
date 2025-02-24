from django.contrib import admin

from apps.api.models import Hotel, Location,Service

# Register your models here.
admin.register(Hotel)
admin.register(Location)
admin.register(Service)