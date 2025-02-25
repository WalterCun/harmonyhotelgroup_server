from django.contrib import admin

from apps.core.models import City, Country, Province


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass
