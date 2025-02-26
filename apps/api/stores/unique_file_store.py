import os
from hashlib import md5
from django.core.files.storage import FileSystemStorage


class UniqueFileStorage(FileSystemStorage):
    """
    Un sistema de almacenamiento que evita duplicados almacenando archivos según su hash MD5.
    Si el archivo ya existe, se reutiliza en lugar de guardar una copia.
    """

    def get_available_name(self, name, max_length=None):
        """
        Sobreescribe el méto-do para asegurarse de que no se creen archivos duplicados.
        No añade sufijos como _1, _2, etc.
        """
        return name  # No cambia el nombre, usamos el hash como nombre único

    def save(self, name, content, max_length=None):
        """
        Guarda el archivo si no existe previamente. Si existe, reutiliza el existente.
        """
        file_hash = self.get_file_hash(content)
        ext = os.path.splitext(name)[-1]
        folder = os.path.dirname(name)
        new_name = f"{folder + '/' if folder else ''}{file_hash}{ext}".strip()

        # Si ya existe, simplemente devuelve la ruta sin guardar nuevamente
        if self.exists(new_name):
            return new_name

        # Guarda el archivo con su hash como nombre
        return super().save(new_name, content, max_length=max_length)

    def delete(self, name):
        """
        Elimina el archivo solo si ya no es referenciado en la base de datos.
        """
        # Importación dentro del méto-do para evitar problemas de importación circular
        from apps.api.models import SocialPlatform
        print('delete: ', name)
        if not SocialPlatform.objects.filter(logo=name).exists():
            super().delete(name)  # Elimina solo si no hay referencias

    @staticmethod
    def get_file_hash(file):
        """Genera un hash MD5 del contenido del archivo."""
        hasher = md5()
        for chunk in file.chunks():
            hasher.update(chunk)
        return hasher.hexdigest()

# Instancia de nuestro almacenamiento personalizado
unique_storage = UniqueFileStorage()
