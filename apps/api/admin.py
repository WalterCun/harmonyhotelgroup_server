from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.api.forms.location_form import HotelForm
from apps.api.models import Hotel, Location, Service


@admin.register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display = ['name', 'location', 'stars', 'is_active']
    form = HotelForm

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "services":
            # Filtra solo los servicios activos
            kwargs["queryset"] = Service.objects.filter(is_active=True)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Location)
class LocationAdmin(ModelAdmin):
    list_filter = ("is_active", "city__province__country", "city__province", "city")
    search_fields = ("main_street", "house_number", "intersection", "city__name")
    ordering = ("city", "main_street")



@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    pass
