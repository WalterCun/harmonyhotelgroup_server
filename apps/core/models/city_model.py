from django.db.models import Model, CharField, DateTimeField, ImageField, ForeignKey, CASCADE, BooleanField

from apps.core.models.province_model import Province


class City(Model):
    name = CharField(max_length=50)
    flag = ImageField(upload_to='flags',null=True,blank=True)
    is_active = BooleanField(default=True)
    province = ForeignKey(Province, related_name="province_city", on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return f'{self.name} ({"Active" if self.is_active else "Desactive"})'

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

