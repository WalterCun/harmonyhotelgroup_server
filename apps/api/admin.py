from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.api.forms.location_form import HotelForm
from apps.api.models import Hotel, Location, Service, Offer, OfferMetric, PageStatistics, OfferTag, ProspectSubject, \
    ProspectSource, Prospect, SocialNetwork, SocialPlatform, TourCategory, PriceType, TourDestination, TourImage, \
    TourVideo


######################################################################################################################
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


######################################################################################################################
@admin.register(OfferMetric)
class OfferMetricAdmin(ModelAdmin):
    pass


@admin.register(PageStatistics)
class PageStatisticsAdmin(ModelAdmin):
    pass


######################################################################################################################
@admin.register(OfferTag)
class OfferTagAdmin(ModelAdmin):
    pass


@admin.register(Offer)
class OfferAdmin(ModelAdmin):
    pass


######################################################################################################################
@admin.register(ProspectSubject)
class ProspectSubjectAdmin(ModelAdmin):
    pass


@admin.register(ProspectSource)
class ProspectSourceAdmin(ModelAdmin):
    pass


@admin.register(Prospect)
class ProspectAdmin(ModelAdmin):
    pass


######################################################################################################################
@admin.register(SocialPlatform)
class SocialPlatformAdmin(ModelAdmin):
    pass


@admin.register(SocialNetwork)
class SocialNetworkAdmin(ModelAdmin):
    pass


######################################################################################################################
@admin.register(TourCategory)
class TourCategoryAdmin(ModelAdmin):
    pass


@admin.register(PriceType)
class PriceTypeAdmin(ModelAdmin):
    pass


@admin.register(TourDestination)
class TourDestinationAdmin(ModelAdmin):
    pass


@admin.register(TourImage)
class TourImageAdmin(ModelAdmin):
    pass


@admin.register(TourVideo)
class TourVideoAdmin(ModelAdmin):
    pass
