from django.contrib import admin

from apps.core.models import City, Country, Province


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("name", "province__name", "province__country__name")


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    search_fields = ("name", "country__name")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
