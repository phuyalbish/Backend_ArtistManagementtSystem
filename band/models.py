from django.db import models

class Band(models.Model):
    bandname = models.CharField(max_length=50, unique=True, null=False)
    name = models.CharField(max_length=50, null=False)
    profile_img = models.ImageField(upload_to='uploads/band/')
    banner_img = models.ImageField(upload_to='uploads/band')
    modified_by = models.CharField(max_length=50, null=True)

    # ASLDKLDAKSL