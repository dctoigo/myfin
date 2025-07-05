from .base import *

DEBUG = env.bool("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

SECRET_KEY = env.str("DJANGO_SECRET_KEY", default="django-insecure-u9^3rp@2%tlmbp)j7p7+1)d*+7v3p@=+oynzx2bw+(ctwbtf87")

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': env.db_url('DATABASE_URL')
}
