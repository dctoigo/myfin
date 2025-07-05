import os

ENVIRONMENT = os.environ.get("DJANGO_ENVIRONMENT", "development")

if ENVIRONMENT == "production":
    from .production import *
elif ENVIRONMENT == "staging":
    from .staging import *
else:
    from .development import *