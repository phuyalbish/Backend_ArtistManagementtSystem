from django.db import models
from rest_framework import serializers


class CustomTheme(models.Model):
    name= models.CharField(max_length=100, null=False, unique=True, default="default")
    secondaryColor = models.CharField(max_length=50, default="#ff4000")
    darkPrimaryColor =  models.CharField(max_length=50, default="#f6f3eb")
    lightPrimaryColor = models.CharField(max_length=50, default="#ECE6D5")
    img_profile = models.ImageField(upload_to='uploads/custombg/', null=True,   default='uploads/default/defaultCustomBg.jpg' )
    is_deleted = models.BooleanField(default=False)

class CustomThemeSerializer(serializers.ModelSerializer):
      class Meta:
        model = CustomTheme
        fields = "__all__"
