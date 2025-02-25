from django.db.models import Model, CharField, ImageField, BooleanField, DateTimeField, ForeignKey, CASCADE

from apps.core.models.country_model import Country


class Province(Model):
    name = CharField(max_length=50)
    flag = ImageField(upload_to='province', blank=True, null=True)
    is_active = BooleanField(default=True)
    country = ForeignKey(Country, related_name="country_province", on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({"Active" if self.is_active else "Desactive"})'
