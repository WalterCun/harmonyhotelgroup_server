from django.db.models import Model, CharField, FloatField, DateTimeField, TextField, ForeignKey, SmallIntegerField, \
    ManyToManyField, CASCADE
from django.utils.translation import gettext_lazy as _


class Location(Model):
    city = CharField(max_length=100)
    country = CharField(max_length=100)
    main_street = CharField(max_length=255)
    house_number = CharField(max_length=20, null=True)
    intersection = CharField(max_length=255, null=True)
    latitude = FloatField(null=True)
    longitude = FloatField(null=True)
    map_url = CharField(max_length=500, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = _("Location")
        verbose_name_plural = _("Location")

class Service(Model):
    name = CharField(max_length=255)
    description = TextField(null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = _("Service")
        verbose_name_plural = _("Service")

class Hotel(Model):
    name = CharField(max_length=255)
    location = ForeignKey(Location, related_name="hotels", on_delete=CASCADE)
    slogan = CharField(max_length=255, null=True)
    stars = SmallIntegerField()
    description = TextField()
    services = ManyToManyField(Service, related_name="hotels")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = _("Hotel")
        verbose_name_plural = _("Hotel")