from django.db import models
from user.models import Users
from rest_framework import serializers


class CustomTheme(models.Model):
    user = models.OneToOneField(Users, null=False, on_delete=models.CASCADE, related_name="user_customizable")
    secondaryColor = models.CharField(max_length=50, default="#ff4000")
    darkPrimaryColor =  models.CharField(max_length=50, default="#f6f3eb")
    lightPrimaryColor = models.CharField(max_length=50, default="#ECE6D5")
    img_profile = models.ImageField(upload_to='uploads/custombg/', null=True,   default='uploads/default/defaultCustomBg.jpg' )


class CustomThemeSerializer(serializers.ModelSerializer):
      class Meta:
        model = CustomTheme
        fields = "__all__"