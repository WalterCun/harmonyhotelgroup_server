from django.db.models import Model, CharField, TextField, EmailField, ForeignKey, PROTECT, DateTimeField
from django.utils.timezone import now


class ProspectSubject(Model):
    """
    Tabla para los posibles asuntos que pueden seleccionar los prospectos al contactar.
    """
    name = CharField(max_length=100, unique=True, help_text="Nombre del asunto. Ej: 'Interés en tours'.")
    description = TextField(blank=True, help_text="Descripción opcional para detallar el asunto.")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Asunto de Prospecto"
        verbose_name_plural = "Asuntos de Prospectos"


class ProspectSource(Model):
    """
    Tabla para registrar las fuentes desde las cuales provienen los prospectos.
    """
    name = CharField(max_length=100, unique=True, help_text="Nombre de la fuente. Ej: 'Web'.")
    description = TextField(blank=True, help_text="Descripción opcional de la fuente.")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fuente de Prospecto"
        verbose_name_plural = "Fuentes de Prospectos"


class Prospect(Model):
    """
    Modelo para registrar prospectos que contactan a través de la página web.
    """
    # Información básica del contacto
    first_name = CharField(max_length=100, help_text="Nombre del prospecto.")
    last_name = CharField(max_length=100, help_text="Apellido del prospecto.")
    email = EmailField(help_text="Correo electrónico del prospecto.")
    phone = CharField(
        max_length=15,
        blank=True,
        null=True,
        help_text="Teléfono móvil del prospecto. Formato internacional permitido (Ej: +593 123456789)."
    )

    # Relación con tablas dinámicas para Asuntos y Fuentes
    subject = ForeignKey(
        ProspectSubject,
        on_delete=PROTECT,
        related_name="prospects",
        help_text="Asunto del mensaje enviado por el prospecto."
    )
    source = ForeignKey(
        ProspectSource,
        on_delete=PROTECT,
        related_name="prospects",
        help_text="Fuente primaria del prospecto."
    )

    # Información acerca del mensaje
    message = TextField(help_text="Mensaje enviado por el prospecto.")

    # Estado del prospecto (para uso interno del seguimiento)
    status_choices = [
        ('nuevo', 'Nuevo'),
        ('en_proceso', 'En Proceso'),
        ('contactado', "Contactado"),
        ('cerrado', 'Cerrado'),
        ('descartado', 'Descartado'),
    ]
    status = CharField(
        max_length=15,
        choices=status_choices,
        default='nuevo',
        help_text="Estatus actual del prospecto en el proceso de seguimiento."
    )

    # Información adicional
    received_at = DateTimeField(default=now, help_text="Fecha y hora en la que se recibió el contacto.")
    notes = TextField(
        blank=True,
        null=True,
        help_text="Notas adicionales para el seguimiento del prospecto. Uso interno."
    )

    # Auditoría
    created_at = DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del registro.")
    updated_at = DateTimeField(auto_now=True, help_text="Última vez que se actualizó el registro.")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject.name} ({self.status})"

    class Meta:
        verbose_name = "Prospecto"
        verbose_name_plural = "Prospectos"
        ordering = ['-received_at']  # Orden por defecto: más recientes primero
