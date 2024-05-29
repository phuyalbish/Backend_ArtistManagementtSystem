from django.db import models
class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)
    modified_by = models.CharField(max_length=50, null=True)