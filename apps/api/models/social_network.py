import imghdr
from hashlib import md5

from django.core.exceptions import ValidationError
from django.db.models import Model, DateTimeField, BooleanField, URLField, CharField, ForeignKey, CASCADE, TextField, \
    FileField

from apps.api.stores.unique_file_store import UniqueFileStorage


def validate_image_or_svg(file):
    """
    Valida que el archivo sea una imagen (JPG, PNG, GIF) o un archivo SVG.
    """
    # Obtenemos el tipo MIME del archivo cargado
    if file.name.endswith('.svg'):
        # El archivo es un SVG válido
        return

        # Si no es SVG, verificamos si es una imagen rasterizada (JPG, PNG, GIF)
    valid_image_types = ['jpeg', 'png', 'gif']
    file_type = imghdr.what(file)  # Detecta el formato de la imagen

    if file_type not in valid_image_types:
        raise ValidationError("Solo se permiten imágenes (JPG, PNG, GIF) o archivos SVG.")
    return


def social_network_upload_path(instance, filename):
    """Genera un nombre de archivo basado en el hash MD5 del contenido para evitar duplicados."""
    if instance.logo:
        file_content = instance.logo.read()
        file_hash = md5(file_content).hexdigest()
        ext = filename.split('.')[-1]
        return f"social_networks/{file_hash}.{ext}"


unique_storage = UniqueFileStorage()  # Instancia de nuestro almacenamiento personalizado


class SocialPlatform(Model):
    """
    Modelo para gestionar dinámicamente las plataformas de redes sociales.
    """
    name = CharField(max_length=50, unique=True)
    description = TextField(null=True, blank=True)
    is_active = BooleanField(default=True)
    logo = FileField(storage=unique_storage, upload_to='social_networks/', null=True, blank=True,
                     validators=[validate_image_or_svg])
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {'🖼️' if self.logo else ''} {'✅' if self.is_active else '❌'}".strip()

    def delete(self, *args, **kwargs):
        """Antes de eliminar, revisa si la imagen ya no es usada en otros registros y elimínala."""
        print('detele model')
        logo_path = self.logo.name if self.logo else None
        super().delete(*args, **kwargs)
        if logo_path and not SocialPlatform.objects.filter(logo=logo_path).exists():
            pass

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
