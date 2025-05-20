# pylint: disable=unused-wildcard-import,wildcard-import
"""
This is the production settings.py where the production enviromnent seetings are placed.
"""


from .base import *

DEBUG = False


STATIC_URL = "static/"
STATIC_ROOT = "staticfiles/"


# Security

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [cors.strip() for cors in env("CORS_ALLOWED_ORIGINS").split(",")]
ALLOWED_HOSTS = [host.strip() for host in env("ALLOWED_HOSTS").split(",")]


# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]


# Databases
DATABASES = {
    "sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "mysql": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("PROD_DB_NAME"),
        "USER": env("PROD_DB_USER"),
        "PASSWORD": env("PROD_DB_PASSWORD"),
        "HOST": env("PROD_DB_HOST"),
        "PORT": env("PROD_DB_PORT"),
        "OPTIONS": {
            "autocommit": True,
        },
    },
    "postgresql": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("PROD_DB_NAME"),
        "USER": env("PROD_DB_USER"),
        "PASSWORD": env("PROD_DB_PASSWORD"),
        "HOST": env("PROD_DB_HOST"),
        "PORT": env("PROD_DB_PORT"),
    },
}


PROD_DEFAULT_DB = env("PROD_DEFAULT_DB", default="sqlite")

DATABASES["default"] = DATABASES[PROD_DEFAULT_DB]
