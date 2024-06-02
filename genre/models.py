from django.db import models
class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)
    is_deleted = models.BooleanField(default=False)
    modified_by = models.IntegerField(null=True)