import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Create a default staff user"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = os.getenv("DJANGO_STAFF_EMAIL")
        password = os.getenv("DJANGO_STAFF_PASSWORD")

        if not User.objects.filter(email=email).exists():
            User.objects.create_user(
                email=email,
                password=password,
                username="staffuser",     
                firstname="Staff",
                lastname="User",
                is_staff=True,
                is_superuser=False,
                is_artist=False,          
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created staff user with email {email}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Staff user with email {email} already exists.")
            )