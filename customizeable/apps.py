from django.apps import AppConfig


class CustomizeableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customizeable'
