from email.policy import default
from .base import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ["*"]


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config('DB_NAME', default='db'),
        "USER": config('DB_USER', default='db'),
        "PASSWORD": config('DB_PASSWORD', default='db'),
        "HOST": config('DB_HOST', default='localhost'),
        "PORT": config('DB_PORT', default=5432),
    }
}

db_from_env = dj_database_url.config('DATABASE_URL')
DATABASES['default'].update(db_from_env)

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:1234',
    'http://localhost:3000',
    'http://localhost:*',
    'http://127.0.0.1:*'
]