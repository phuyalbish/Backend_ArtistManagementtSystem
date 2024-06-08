from django.db import models
from user.models import Users


class CustomTheme(models.Model):
    user = models.OneToOneField(Users, null=False, on_delete=models.CASCADE)
    secondaryColor = models.CharField(max_length=50, default="#ff4000")
    darkPrimaryColor =  models.CharField(max_length=50, default="#f6f3eb")
    lightPrimaryColor = models.CharField(max_length=50, default="#ECE6D5")
    bgImage  = models.ImageField()
