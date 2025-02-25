from django.db.models import Model, DateTimeField, BooleanField, URLField, CharField, ForeignKey, CASCADE, TextField


class SocialPlatform(Model):
    """
    Modelo para gestionar dinámicamente las plataformas de redes sociales.
    """
    name = CharField(max_length=50, unique=True)
    description = TextField(null=True, blank=True)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plataforma de Red Social"
        verbose_name_plural = "Plataformas de Redes Sociales"


class SocialNetwork(Model):
    hotel = ForeignKey(
        'Hotel',
        related_name='hotel_social_networks',
        on_delete=CASCADE
    )
    platform = ForeignKey(
        SocialPlatform,
        related_name='social_networks',
        on_delete=CASCADE
    )
    url = URLField()
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hotel.name} - {self.platform}"

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        unique_together = ('hotel', 'platform')
