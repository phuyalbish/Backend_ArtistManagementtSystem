"""
this file combines the appropriate environment to the base.py according to the env
"""

import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DJANGO_ENV=(str, "development"),
)


environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


DJANGO_ENV = os.environ.get("DJANGO_ENV")


ENVIRONMENT = env("DJANGO_ENV")
print(ENVIRONMENT)

if ENVIRONMENT == "development":
    from .development import *
else:
    from .production import *
