from pathlib import Path

from django.core.management import BaseCommand, call_command

from apps.commands.utils.plural import plural
from apps.commands.utils.searchs import list_models, find_fixture


class Command(BaseCommand):
    help = 'Sync backup fixtures .....'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('Generando backups for database...')
        self.stdout.write('Extraiendo modelos')
        backups_models = list_models(['auth.user'])
        self.stdout.write('Buscando directorio de fixtures')
        fixtures_dir = find_fixture()

        for model in backups_models:
            for key, value in fixtures_dir.items():
                if key in model:
                    backup_file = f'{fixtures_dir.get(key) / plural(Path(model.split(".")[-1]))}.json'
                else:
                    backup_file = f'{next(iter(fixtures_dir.values())) / plural(Path(model.split(".")[-1]))}.json'
                self.stdout.write(f'Cargando fixtures en directorios del modelo: {model}')
                call_command('dumpdata', model, '--output', backup_file, '--indent', '4')
