import re

from django.core.exceptions import ValidationError
from django.db.models import Model, CharField, FloatField, DateTimeField, TextField, ForeignKey, SmallIntegerField, \
    ManyToManyField, CASCADE, BooleanField
from django.utils.translation import gettext_lazy as _


def validate_house_number(value):
    """
    Valida que el valor de house_number sea:
    - Una combinación de valores numéricos separados por `-`
    - La palabra "s/n" (en mayúsculas o minúsculas)
    """
    if not re.match(r'^(\d+(-\d+)?|s/n|S/N)$', value):
        raise ValidationError(
            'Este campo solo permite valores numéricos separados por "-" o "s/n".',
            params={'value': value},
        )


class Location(Model):
    city = ForeignKey("core.City", related_name="cities", on_delete=CASCADE)
    main_street = CharField(max_length=255)
    house_number = CharField(max_length=10, default='S/N', validators=[validate_house_number])
    intersection = CharField(max_length=255, null=True, blank=True, )
    latitude = FloatField(default=0.0)
    longitude = FloatField(default=0.0)
    map_url = CharField(max_length=250, null=True, blank=True)
    is_assigned = BooleanField(default=False)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.main_street} {self.house_number if self.house_number else ''} "
                f"{'y ' + self.intersection if self.intersection else ''}, {self.city.name}, {self.city.province.name},"
                f"{self.city.province.country.name}").strip()

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")


class Service(Model):
    name = CharField(max_length=255)
    description = TextField(null=True, blank=True, )
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.is_active})'

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")


class Hotel(Model):
    name = CharField(max_length=255)
    location = ForeignKey(Location, related_name="hotels", on_delete=CASCADE)
    slogan = CharField(max_length=255, null=True, blank=True, )
    stars = CharField(max_length=1, choices=[('1', '🌟'), ('2', '🌟🌟'), ('3', '🌟🌟🌟'), ('4', '🌟🌟🌟🌟'), ('5', '🌟🌟🌟🌟🌟')])
    description = TextField(null=True, blank=True,)
    services = ManyToManyField(Service, related_name="hotels")
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.location})'

    class Meta:
        verbose_name = _("Hotel")
        verbose_name_plural = _("Hotels")
