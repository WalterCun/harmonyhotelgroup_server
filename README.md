# HarmonyHotel Service

## Descripción
HarmonyHotel Service es un backend desarrollado en Django que proporciona una API REST para gestionar hoteles, incluyendo información sobre ubicaciones, descripciones y calificaciones.

## Estructura del Proyecto
```
HarmonyHotel_Service/
│── api/                    # Aplicación principal
│   ├── migrations/         # Migraciones de la base de datos
│   ├── __init__.py
│   ├── admin.py            # Configuración del panel de administración
│   ├── apps.py             # Configuración de la app
│   ├── models.py           # Modelos de la base de datos
│   ├── serializers.py      # Serialización de datos (DRF)
│   ├── tests.py            # Pruebas unitarias
│   ├── urls.py             # Rutas específicas de la app
│   ├── views.py            # Controladores de la API
│── harmonyhotel_service/    # Configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py             # Configuración ASGI (Para WebSockets y más)
│   ├── settings.py         # Configuración global del proyecto
│   ├── urls.py             # Rutas globales del proyecto
│   ├── wsgi.py             # Configuración WSGI (Para producción)
│── manage.py               # Archivo para ejecutar comandos de Django
│── requirements.txt        # Dependencias del proyecto
```

## Instalación
### 1. Crear el entorno virtual
```sh
uv venv django_env
uv pip install -r requirements.txt
```

### 2. Aplicar las migraciones de la base de datos
```sh
python manage.py migrate
```

### 3. Crear un superusuario (opcional, para administrar el panel de Django)
```sh
python manage.py createsuperuser
```

### 4. Ejecutar el servidor
```sh
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/api/`

## Endpoints Principales
| Método | Endpoint | Descripción |
|---------|----------|-------------|
| GET | `/api/hoteles/` | Lista todos los hoteles |
| POST | `/api/hoteles/` | Crea un nuevo hotel |
| GET | `/api/hoteles/{id}/` | Obtiene un hotel por su ID |
| PUT | `/api/hoteles/{id}/` | Actualiza un hotel |
| DELETE | `/api/hoteles/{id}/` | Elimina un hotel |

## Dependencias
```
Django
djangorestframework
```

## Contacto
Si tienes dudas o sugerencias, contáctanos a soporte@harmonyhotel.com

