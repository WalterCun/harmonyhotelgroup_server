from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, DateTimeField, DecimalField, ImageField, \
    ManyToManyField, PositiveSmallIntegerField, PositiveIntegerField, BooleanField


class OfferTag(Model):
    """
    Modelo para las etiquetas asociadas a las ofertas (Ej: Promoción, Descuento, Temporada Baja, etc.).
    """
    name = CharField(max_length=50, unique=True)
    description = TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Etiqueta de Oferta"
        verbose_name_plural = "Etiquetas de Ofertas"


class Offer(Model):
    """
    Modelo para las ofertas asociadas a un hotel.
    """
    hotel = ForeignKey(
        'Hotel',
        related_name='offers',
        on_delete=CASCADE
    )
    title = CharField(max_length=100)  # Título de la oferta
    description = TextField()  # Descripción detallada de la oferta
    start_date = DateTimeField(null=True, blank=True)  # Inicio de validez de la oferta
    end_date = DateTimeField()  # Caducidad de la oferta
    original_price = DecimalField(max_digits=10, decimal_places=2)  # Precio original del producto o servicio
    promotional_price = DecimalField(max_digits=10, decimal_places=2)  # Precio con descuento
    discount_percentage = DecimalField(max_digits=5, decimal_places=2, null=True,
                                              blank=True)  # Porcentaje de descuento
    image = ImageField(upload_to='offers/', null=True, blank=True)  # Imagen promocional de la oferta
    tags = ManyToManyField(OfferTag, related_name='offers', blank=True)  # Etiquetas de la oferta
    terms_and_conditions = TextField(null=True, blank=True)  # Términos y condiciones de la oferta
    priority = PositiveSmallIntegerField(default=0)  # Prioridad para ordenar las ofertas
    stock = PositiveIntegerField(null=True, blank=True)  # Cantidad limitada de la oferta (opcional)

    # Métricas de la oferta para conocer su aceptación
    views_count = PositiveIntegerField(default=0)  # Número de vistas de la oferta
    interactions_count = PositiveIntegerField(default=0)  # Número de interacciones (clics o similar)
    redemption_count = PositiveIntegerField(default=0)  # Número de redenciones/reclamos de la oferta

    # Estado y auditoría
    is_active = BooleanField(default=True)  # Determina si la oferta está activa
    created_at = DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = DateTimeField(auto_now=True)  # Última actualización

    def __str__(self):
        return f"{self.hotel.name} - {self.title}"

    @property
    def calculate_discount_percentage(self):
        """
        Calcula el porcentaje de descuento si no está directamente definido.
        """
        if self.original_price and self.promotional_price:
            return round((1 - (self.promotional_price / self.original_price)) * 100, 2)
        return None

    @property
    def acceptance_rate(self):
        """
        Calcula una tasa de aceptación basada en las interacciones y redenciones.
        Si hay interacciones, utiliza la fórmula: (redenciones / interacciones) * 100
        """
        if self.interactions_count > 0:
            return round((self.redemption_count / self.interactions_count) * 100, 4)
        return 0.0

    class Meta:
        verbose_name = "Oferta"
        verbose_name_plural = "Ofertas"
        ordering = ['-priority', '-views_count',
                    'end_date']  # Ordenar por prioridad y luego vistas, seguido de fecha final