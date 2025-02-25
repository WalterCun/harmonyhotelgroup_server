from django import forms
from django.db.models import Q

from apps.api.models import Hotel


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        # Obtener la instancia del modelo actual
        instance = kwargs.get("instance")
        super().__init__(*args, **kwargs)

        # Verifica y ajusta el queryset dinámico
        if instance and instance.location:
            # Si ya hay una location seleccionada, inclúyela en el queryset
            self.fields['location'].queryset = self.fields['location'].queryset.filter(
                Q(is_assigned=False) | Q(pk=instance.location.pk)
            )
        else:
            # Si es un nuevo registro, solo muestra las no asignadas
            self.fields['location'].queryset = self.fields['location'].queryset.filter(is_assigned=False)

    def save(self, commit=True):
        # Obtener la instancia previa (edición)
        instance = self.instance
        print(self.cleaned_data["location"])
        # Verificar si se está cambiando la location
        if instance.pk:  # Registro existente
            previous_location = instance.location  # La location anterior
            new_location = self.cleaned_data["location"]  # La nueva seleccionada

            if previous_location and previous_location != new_location:
                # Cambiar la anterior a is_assigned=False
                previous_location.is_assigned = False
                previous_location.save()

            # Guardar el resto del formulario
            return super().save(commit)

        # Cambiar la nueva location a is_assigned=True
        location = self.cleaned_data["location"]
        if location:
            location.is_assigned = True
            location.save()

        # Guardar el resto del formulario
        return super().save(commit)
