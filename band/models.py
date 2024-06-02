from django.db import models
from user.models import Users
class Band(models.Model):
    bandname = models.CharField(max_length=50, null=False,  unique=True)
    description = models.CharField(max_length=150, null=False)
    name = models.CharField(max_length=50, null=False)
    is_deleted = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    profile_img = models.ImageField(upload_to='uploads/band/', null=True)
    banner_img = models.ImageField(upload_to='uploads/band', null=True)
    modified_by = models.IntegerField( null=True)


class BandMember(models.Model):
    band =  models.ForeignKey(Band, on_delete=models.CASCADE, related_name='members',)
    artist =  models.OneToOneField(Users, on_delete=models.CASCADE)
