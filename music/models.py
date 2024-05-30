from django.utils import timezone 
from django.db import models

from genre.models import Genre
from album.models import Album
from band.models import Band
from user.models import Users
class Music(models.Model):
    name = models.CharField(max_length=50, null=False)
    description =  models.CharField(max_length=50, null=False)
    img_profile = models.ImageField(upload_to='uploads/music/', null=True)
    language = models.CharField(max_length=50, null=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(Users, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    totallike = models.IntegerField(default=0)
    totalcomment = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    release_at = models.DateTimeField(default=timezone.now)
    music_file = models.FileField( upload_to =  'uploads/', null=True )
    is_hidden = models.BooleanField(default=0)
    is_deleted = models.BooleanField(default=0)
    is_released = models.BooleanField(default=0)
    is_disabled = models.BooleanField(default=0)
    modified_by = models.CharField(max_length=50, null=True)

