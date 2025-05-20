# pylint: disable=unused-wildcard-import,wildcard-import

"""
This is the development settings.py where the development enviromnent seetings are placed.
"""


from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True


DATABASES = {
    "sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "mysql": {
        "NAME": env("DEV_DB_NAME"),
        "ENGINE": "django.db.backends.mysql",
        "HOST": env("DEV_DB_HOST"),
        "PORT": env("DEV_DB_PORT"),
        "USER": env("DEV_DB_USER"),
        "PASSWORD": env("DEV_DB_PASSWORD"),
        "OPTIONS": {
            "autocommit": True,
        },
    },
    "postgresql": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DEV_DB_NAME"),
        "USER": env("DEV_DB_USER"),
        "PASSWORD": env("DEV_DB_PASSWORD"),
        "HOST": env("DEV_DB_HOST"),
        "PORT": env("DEV_DB_PORT"),
    },
}


STATIC_URL = "static/"
STATIC_ROOT = "staticfiles/"

DEV_DEFAULT_DB = env("DEV_DEFAULT_DB", default="sqlite")

DATABASES["default"] = DATABASES[DEV_DEFAULT_DB]
