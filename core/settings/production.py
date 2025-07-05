from .base import *


# Debug e Hosts permitidos
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['myfin.local', 'myfin.squadra.dev.br', 'myfin.diogotoigo.dev.br'])

