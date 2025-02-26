from django.db.models import CharField, DateField, Model, OneToOneField, CASCADE, PositiveIntegerField, DateTimeField, \
    FloatField, DecimalField
from django.utils.timezone import now


class OfferMetric(Model):
    """
    Modelo para métricas generales relacionadas con las ofertas (sin usuarios específicos).
    """
    offer = OneToOneField(
        'Offer',
        on_delete=CASCADE,
        related_name='metrics'
    )

    # Métricas Totales
    total_views = PositiveIntegerField(
        default=0,
        help_text="Número total de visualizaciones de la oferta, incluyendo visitas repetidas."
    )
    total_interactions = PositiveIntegerField(
        default=0,
        help_text="Número total de interacciones (clics en 'ver más')."
    )
    total_redemptions = PositiveIntegerField(
        default=0,
        help_text="Número total de redenciones de la oferta."
    )

    # Datos Totales Por Canal
    from_social_media = PositiveIntegerField(
        default=0,
        help_text="Número de visitas provenientes de redes sociales."
    )
    from_direct_traffic = PositiveIntegerField(
        default=0,
        help_text="Número de visitas directas."
    )
    from_other_sources = PositiveIntegerField(
        default=0,
        help_text="Número de visitas provenientes de otras fuentes."
    )

    # Auditoría
    created_at = DateTimeField(default=now, help_text="Fecha de creación del registro de métricas.")
    updated_at = DateTimeField(auto_now=True, help_text="Última actualización del registro de métricas.")

    def __str__(self):
        return f"Métricas Generales para la oferta {self.offer.title}"

    class Meta:
        verbose_name = "Métrica General de Oferta"
        verbose_name_plural = "Métricas Generales de Ofertas"


class PageStatistics(Model):
    """
    Modelo para estadísticas agregadas (promedios, tasas, tiempos) de una oferta.
    """
    page = CharField(max_length=25, null=True, blank=True, help_text='Url de la pagina a extraer datos de sondeo')

    sample = DateField(auto_now_add=True, null=True, help_text='Fecha de captura de datos')

    # Estadísticas Promediadas
    average_time_on_page = FloatField(
        null=True, blank=True,
        help_text="Tiempo promedio (en segundos) que los usuarios pasan en la página de la oferta."
    )
    abandonment_rate = DecimalField(
        max_digits=5, decimal_places=2,
        null=True, blank=True,
        help_text="Porcentaje de usuarios que interactúan pero abandonan sin redimir."
    )
    conversion_rate = DecimalField(
        max_digits=5, decimal_places=2,
        null=True, blank=True,
        help_text="Porcentaje de vistas que resultan en redenciones."
    )

    # Estadísticas relacionadas con ingresos
    average_revenue_per_redemption = DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True,
        help_text="Ingresos promedio generados por cada redención."
    )
    estimated_total_revenue = DecimalField(
        max_digits=10, decimal_places=2,
        default=0.0,
        help_text="Ingreso estimado total basado en las redenciones."
    )

    # Estadísticas Futuras por Usuario (opcional, para futuro registro de usuarios)
    visits_by_new_users = PositiveIntegerField(
        null=True, blank=True,
        help_text="Visitas estimadas de usuarios nuevos."
    )
    visits_by_returning_users = PositiveIntegerField(
        null=True, blank=True,
        help_text="Visitas estimadas de usuarios recurrentes."
    )

    def __str__(self):
        return f"Estadísticas Proporcionadas para {self.page}"

    class Meta:
        verbose_name = "Estadística Agregada de Oferta"
        verbose_name_plural = "Estadísticas de Oferta"
