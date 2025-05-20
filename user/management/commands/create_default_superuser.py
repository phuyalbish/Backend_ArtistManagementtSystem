import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a default superuser"

    def handle(self, *args, **kwargs):
        user = get_user_model()
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not user.objects.filter(email=email).exists():
            user.objects.create_superuser(email=email, password=password)
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created superuser with email {email}")
            )
