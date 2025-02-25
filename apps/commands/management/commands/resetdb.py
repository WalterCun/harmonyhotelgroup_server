import shutil
from pathlib import Path

from django.conf import settings
from django.core.management import BaseCommand, call_command

from apps.commands.utils.searchs import find_fixture_files


def delete(file_path: Path):
    try:
        # Verificar si el archivo existe antes de eliminarlo
        if file_path.is_file():  # Comprueba si realmente es un archivo
            shutil.rmtree(file_path)
            print(f"El archivo '{file_path}' ha sido eliminado.")
        else:
            print(f"El archivo '{file_path}' no existe o no es un archivo.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar el archivo: {e}")


class Command(BaseCommand):
    help = 'Reset the database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('Resetting database...')
        # call_command('backup')

        # fix = find_fixture_files()

        if settings.DEBUG:
            delete(settings.DATABASES.get('default').get('NAME'))

            self.stdout.write("Ejecutando 'makemigrations'...")
            call_command("makemigrations", 'api', 'core')

            self.stdout.write("Ejecutando 'migrate'...")
            call_command('migrate')

            # for files in fix.values():
            #     # load = [file.name for file in files]
            for file in ['countries', 'provinces', 'cities', 'superuser', 'services', 'locations',
                         'hoteles']:
                try:
                    self.stdout.write(f"Ejecutando cargando informacion .....")
                    call_command('loaddata', file)
                except Exception as e:
                    print(e)

        self.stdout.write(self.style.SUCCESS("¡Proyecto configurado correctamente!"))
