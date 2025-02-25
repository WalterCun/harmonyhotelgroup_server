from django.db import models
from django.utils.timezone import now


class OfferMetric(models.Model):
    """
    Modelo para métricas generales relacionadas con las ofertas (sin usuarios específicos).
    """
    offer = models.OneToOneField(
        'Offer',
        on_delete=models.CASCADE,
        related_name='metrics'
    )

    # Métricas Totales
    total_views = models.PositiveIntegerField(
        default=0,
        help_text="Número total de visualizaciones de la oferta, incluyendo visitas repetidas."
    )
    total_interactions = models.PositiveIntegerField(
        default=0,
        help_text="Número total de interacciones (clics en 'ver más')."
    )
    total_redemptions = models.PositiveIntegerField(
        default=0,
        help_text="Número total de redenciones de la oferta."
    )

    # Datos Totales Por Canal
    from_social_media = models.PositiveIntegerField(
        default=0,
        help_text="Número de visitas provenientes de redes sociales."
    )
    from_direct_traffic = models.PositiveIntegerField(
        default=0,
        help_text="Número de visitas directas."
    )
    from_other_sources = models.PositiveIntegerField(
        default=0,
        help_text="Número de visitas provenientes de otras fuentes."
    )

    # Auditoría
    created_at = models.DateTimeField(default=now, help_text="Fecha de creación del registro de métricas.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Última actualización del registro de métricas.")

    def __str__(self):
        return f"Métricas Generales para la oferta {self.offer.title}"

    class Meta:
        verbose_name = "Métrica General de Oferta"
        verbose_name_plural = "Métricas Generales de Ofertas"


class PageStatistics(models.Model):
    """
    Modelo para estadísticas agregadas (promedios, tasas, tiempos) de una oferta.
    """
    offer_metric = models.OneToOneField(
        'OfferMetric',
        on_delete=models.CASCADE,
        related_name='statistics'
    )

    # Estadísticas Promediadas
    average_time_on_page = models.FloatField(
        null=True, blank=True,
        help_text="Tiempo promedio (en segundos) que los usuarios pasan en la página de la oferta."
    )
    abandonment_rate = models.DecimalField(
        max_digits=5, decimal_places=2,
        null=True, blank=True,
        help_text="Porcentaje de usuarios que interactúan pero abandonan sin redimir."
    )
    conversion_rate = models.DecimalField(
        max_digits=5, decimal_places=2,
        null=True, blank=True,
        help_text="Porcentaje de vistas que resultan en redenciones."
    )

    # Estadísticas relacionadas con ingresos
    average_revenue_per_redemption = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True,
        help_text="Ingresos promedio generados por cada redención."
    )
    estimated_total_revenue = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=0.0,
        help_text="Ingreso estimado total basado en las redenciones."
    )

    # Estadísticas Futuras por Usuario (opcional, para futuro registro de usuarios)
    visits_by_new_users = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Visitas estimadas de usuarios nuevos."
    )
    visits_by_returning_users = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Visitas estimadas de usuarios recurrentes."
    )


def __str__(self):
    return f"Estadísticas Proporcionadas para {self.offer_metric.offer.title}"


class Meta:
    verbose_name = "Estadística Agregada de Oferta"
    verbose_name_plural = "Estadísticas de Oferta"
