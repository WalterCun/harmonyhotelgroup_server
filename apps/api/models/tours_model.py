from django.db.models import Model, CharField, TextField, DateTimeField, ManyToManyField, DecimalField, ForeignKey, \
    PROTECT, DurationField, BooleanField, CASCADE, ImageField, URLField
from django.utils.timezone import now


class TourCategory(Model):
    """
    Categorías para clasificar los tours/destinos.
    """
    name = CharField(max_length=50, unique=True, help_text="Nombre de la categoría. Ej: 'Cultural'")
    description = TextField(blank=True, help_text="Descripción opcional para la categoría.")
    created_at = DateTimeField(default=now, help_text="Fecha de creación de la categoría.")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría de Tour"
        verbose_name_plural = "Categorías de Tours"


class PriceType(Model):
    """
    Tipos de precios utilizados en los tours.
    """
    name = CharField(max_length=50, unique=True, help_text="Nombre del tipo de precio. Ej: 'Por Persona'")
    description = TextField(blank=True, help_text="Descripción opcional del tipo de precio.")
    created_at = DateTimeField(default=now, help_text="Fecha de creación del tipo de precio.")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Precio"
        verbose_name_plural = "Tipos de Precios"


class TourDestination(Model):
    """
    Modelo para registrar destinos turísticos y tours asociados a uno o más hoteles.
    """
    # Información básica del destino
    title = CharField(max_length=255,
                             help_text="Título del destino o tour. Ej: 'Ruta por el Cañón del Sumidero'")
    description = TextField(help_text="Descripción detallada del destino o actividad.")
    tags = CharField(
        max_length=255,
        blank=True,
        help_text="Etiquetas separadas por comas para facilitar la búsqueda. Ej: 'cultural, aventura, naturaleza'"
    )

    # Relación con hoteles
    hotels = ManyToManyField(
        'Hotel',
        related_name='tours',
        help_text="Hoteles asociados al tour."
    )

    # Información de precios
    price = DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Precio del tour o actividad (sin formato de moneda)."
    )
    price_type = ForeignKey(
        PriceType,
        on_delete=PROTECT,
        related_name="tours",
        help_text="Tipo de precio aplicado al tour."
    )

    # Información del destino
    location = CharField(max_length=255,
                                help_text="Ubicación o lugar del destino. Ej: 'Chiapa de Corzo, Chiapas'")
    duration = DurationField(
        help_text="Duración del tour (en formato hh:mm:ss). Ej: Un tour de 3 horas sería 03:00:00."
    )
    category = ForeignKey(
        TourCategory,
        on_delete=PROTECT,
        related_name="tours",
        help_text="Categoría principal del tour o destino."
    )

    # Estado
    is_active = BooleanField(default=True, help_text="Define si este tour está activo para su publicación.")

    # Auditoría
    created_at = DateTimeField(default=now, help_text="Fecha de creación del tour.")
    updated_at = DateTimeField(auto_now=True, help_text="Última actualización del tour.")

    def __str__(self):
        return f"{self.title} - {self.location}"

    class Meta:
        verbose_name = "Destino Turístico/Tour"
        verbose_name_plural = "Destinos Turísticos/Tours"


class TourImage(Model):
    """
    Imágenes asociadas a cada destino turístico/tour.
    """
    tour = ForeignKey(
        TourDestination,
        on_delete=CASCADE,
        related_name="images",
        help_text="El tour al que pertenece esta imagen."
    )
    image = ImageField(
        upload_to="tour_destinations/",
        help_text="Imagen representativa del destino o tour."
    )
    created_at = DateTimeField(default=now, help_text="Fecha en la que se subió la imagen.")

    def __str__(self):
        return f"Imagen de {self.tour.title}"


class TourVideo(Model):
    """
    Videos asociados a cada destino turístico/tour.
    """
    tour = ForeignKey(
        TourDestination,
        on_delete=CASCADE,
        related_name="videos",
        help_text="El tour al que pertenece este video."
    )
    video_url = URLField(
        help_text="URL del video (YouTube, Facebook, Instagram u otra plataforma)."
    )
    created_at = DateTimeField(default=now, help_text="Fecha en la que se subió el video.")

    def __str__(self):
        return f"Video de {self.tour.title}"