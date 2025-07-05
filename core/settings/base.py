import os
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DJANGO_ENVIRONMENT = os.environ.get('DJANGO_ENVIRONMENT', 'development')

env = environ.Env(DEBUG=(bool, False))

env_files = {
    'development': '.env.development',
    'staging': '.env.staging',
    'production': '.env.production',
}
env_file = env_files.get(DJANGO_ENVIRONMENT)
if env_file:
    env_path = BASE_DIR / env_file
    if env_path.exists():
        environ.Env.read_env(env_path)

# Utilitário para leitura de secrets
def get_secret(key, default=None):
    """Lê secrets via Docker Swarm, variáveis de ambiente ou .env"""
    secret_path = Path(f'/run/secrets/{key}')
    if secret_path.exists():
        return secret_path.read_text().strip()
    
    env_var = os.environ.get(key)
    if env_var:
        return env_var

    try:
        return env(key)
    except environ.ImproperlyConfigured:
        if DJANGO_ENVIRONMENT == 'development':
            return env(key, default=default)
        raise RuntimeError(f'Secret "{key}" não encontrado.')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u9^3rp@2%tlmbp)j7p7+1)d*+7v3p@=+oynzx2bw+(ctwbtf87'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': env('DJANGO_DB_ENGINE', default='django.db.backends.postgresql'),
        'NAME': get_secret('DJANGO_DB_NAME'),
        'USER': get_secret('DJANGO_DB_USER'),
        'PASSWORD': get_secret('DJANGO_DB_PASSWORD'),
        'HOST': get_secret('DJANGO_DB_HOST'),
        'PORT': env.int('DJANGO_DB_PORT', default=5432),
     }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
