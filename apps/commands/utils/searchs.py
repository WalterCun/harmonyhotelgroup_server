from pathlib import Path
from typing import Any

from django.apps import apps
from django.conf import settings


def find_fixture():
    fixtures = {}

    # Obtener la ruta raíz de la carpeta 'apps'
    apps_path = settings.BASE_DIR / "apps"
    # Verificar si la carpeta 'apps' existe
    if not apps_path.exists() or not apps_path.is_dir():
        raise FileNotFoundError(f"La carpeta 'apps' no existe en {settings.BASE_DIR}")

    for app_dir in apps_path.iterdir():

        if app_dir.is_dir():  # Solo buscar en directorios
            fixtures_path = app_dir / "fixtures"

            # Verificar si existe la carpeta 'fixtures'
            if fixtures_path.exists() and fixtures_path.is_dir():
                fixtures[app_dir.name] = fixtures_path

    return fixtures

def find_fixture_files(extension="json") -> dict[Any, list[Path]]:
    """
    Busca archivos de fixtures en la carpeta 'fixtures' de todas las aplicaciones en 'apps',
    que se encuentra bajo BASE_DIR.

    Args:
        extension (str): Extensión de archivo a buscar (por defecto: 'json').

    Returns:
        dict: Un diccionario donde las claves son las rutas de las aplicaciones y los valores
              son listas de rutas de los fixtures encontrados.
    """
    fixtures = {}

    # Obtener la ruta raíz de la carpeta 'apps'
    apps_path = settings.BASE_DIR / "apps"
    # Verificar si la carpeta 'apps' existe
    if not apps_path.exists() or not apps_path.is_dir():
        raise FileNotFoundError(f"La carpeta 'apps' no existe en {settings.BASE_DIR}")

    # Iterar sobre los directorios dentro de 'apps'
    for app_dir in apps_path.iterdir():

        if app_dir.is_dir():  # Solo buscar en directorios
            fixtures_path = app_dir / "fixtures"

            # Verificar si existe la carpeta 'fixtures'
            if fixtures_path.exists() and fixtures_path.is_dir():
                # Buscar archivos con la extensión especificada
                fixture_files = [
                    Path(file) for file in fixtures_path.iterdir()
                    if file.is_file() and file.suffix == f".{extension}"
                ]

                if fixture_files:
                    fixtures[app_dir.name] = fixture_files

    return fixtures


def list_models(search_model_name: list[str]) -> list[str]:
    """
    Lista los modelos definidos en la carpeta 'apps' del proyecto.
    También permite buscar un modelo específico.

    Args:
        search_model_name (str, opcional): Nombre del modelo a buscar (sensible a mayúsculas/minúsculas).
                                            Si no se proporciona, lista todos los modelos.

    Returns:
        None: Imprime los resultados directamente.
    """
    # Ruta base de la carpeta 'apps'
    apps_path = settings.BASE_DIR / "apps"

    # Verificar si la carpeta 'apps' existe
    if not apps_path.exists() or not apps_path.is_dir():
        raise FileNotFoundError(f"La carpeta 'apps' no existe en {settings.BASE_DIR}")

    # Buscar todos los archivos 'models.py' en subcarpetas de 'apps'
    all_models = apps.get_models()
    apps_config = settings.LOCAL_APPS
    name_apps = [name for _apps in apps_config for app, name in [_apps.split('.')]]
    # model_files = apps_path.glob("*/models.py")

    found_models = [] + search_model_name  # Lista donde se guardarán los modelos encontrados

    for model in all_models:
        match = set(name_apps) & set(str(model._meta).split('.'))
        if match:
            found_models.append(str(model._meta))

    # print("Modelos encontrados:")
    # for model in found_models:
    #     print(f" - {model}")
    return found_models
