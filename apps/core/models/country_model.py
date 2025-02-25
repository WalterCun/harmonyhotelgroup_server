from django.db.models import Model, CharField, BooleanField, ForeignKey, DateTimeField, CASCADE


class Country(Model):
    name = CharField(max_length=100)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return f'{self.name} ({"Active" if self.is_active else "Desactive"})'

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"