from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "forex_backend",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

CORS_ORIGIN_WHITELIST = [
    'http://localhost:1234',
    'http://localhost:3000',
    'http://localhost:*',
    'http://127.0.0.1:*'
]