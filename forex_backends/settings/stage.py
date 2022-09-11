from .base import *
from email.policy import default
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

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




sentry_sdk.init(
    dsn="https://9ba768c8cfa347e682796df73e4ac967@o1116976.ingest.sentry.io/6738467",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)