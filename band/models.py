from django.db import models
from user.models import Users
class Band(models.Model):
    bandname = models.CharField(max_length=50, null=False,  unique=True)
    description = models.TextField(null=False)
    name = models.CharField(max_length=50, null=False)
    is_deleted = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    img_cover = models.ImageField(upload_to='uploads/band/cover/', null=True, default='uploads/default/cover.jpeg' )
    img_profile = models.ImageField(upload_to='uploads/band/profile/', null=True,   default='uploads/default/defaultBand.png' )

    modified_by = models.IntegerField( null=True)


class BandMember(models.Model):
    band =  models.ForeignKey(Band, on_delete=models.CASCADE, related_name='members',)
    artist =  models.OneToOneField(Users, on_delete=models.CASCADE)
