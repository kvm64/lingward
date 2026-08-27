import os
from pathlib import Path
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# --- БЕЗОПАСНОСТЬ ---
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']

# --- ПРИЛОЖЕНИЯ ---
INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.crm',
]

# --- ПРОМЕЖУТОЧНЫЙ СЛОЙ ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- МАРШРУТЫ ---
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

# --- БАЗА ДАННЫХ ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- ШАБЛОНЫ ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- ЛОКАЛИЗАЦИЯ ---
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# --- СТАТИКА И МЕДИА ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- НАСТРОЙКИ UNFOLD ---
UNFOLD = {
    "SITE_TITLE": "LINGWARD CRM",
    "SITE_HEADER": "Управление платформой",
    "SITE_URL": "/",
    "THEME": "dark",
    "COLORS": {
        "primary": {
            "50": "250, 245, 255",
            "100": "243, 232, 255",
            "200": "229, 211, 255",
            "300": "209, 186, 255",
            "400": "184, 158, 255",
            "500": "108, 92, 231",
            "600": "88, 72, 211",
            "700": "68, 52, 191",
            "800": "48, 32, 171",
            "900": "28, 12, 151",
        },
        "secondary": {
            "50": "240, 255, 255",
            "100": "220, 255, 255",
            "200": "180, 255, 255",
            "300": "140, 255, 255",
            "400": "100, 255, 255",
            "500": "0, 206, 201",
            "600": "0, 186, 181",
            "700": "0, 166, 161",
            "800": "0, 146, 141",
            "900": "0, 126, 121",
        },
    },
}

# --- КАСТОМНАЯ МОДЕЛЬ ПОЛЬЗОВАТЕЛЯ ---
AUTH_USER_MODEL = 'crm.User'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'