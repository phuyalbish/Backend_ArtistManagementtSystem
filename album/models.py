from django.utils import timezone
from django.db import models
from user.models import Users
from band.models  import Band
class Album(models.Model):
    name = models.CharField(max_length=50, null=False)
    description =  models.TextField( null=False)
    img_cover = models.ImageField(upload_to='uploads/album/cover/', null=True, default='uploads/default/cover.jpeg' )
    img_profile = models.ImageField(upload_to='uploads/album/profile/', null=True,   default='uploads/default/defaultMusic.jpg' )
    artist = models.ForeignKey(Users, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)
    release_at = models.DateTimeField(default=timezone.now)
    totallike = models.IntegerField(default=0)
    totalmusic = models.IntegerField(default=0)
    is_hidden = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_released = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    modified_by = models.IntegerField(null=True)
   


