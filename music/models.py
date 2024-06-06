from django.utils import timezone 
from django.db import models
from genre.models import Genre
from album.models import Album
from band.models import Band
from user.models import Users

class Music(models.Model):
    name = models.CharField(max_length=50, null=False)
    description =  models.TextField(null=False)
    img_profile = models.ImageField(upload_to='uploads/music/image/', null=True)
    language = models.CharField(max_length=50, null=True)
    lyrics= models.TextField(null=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(Users, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)
    release_at = models.DateTimeField(default=timezone.now)
    music_file = models.FileField( upload_to =  'uploads/music/', null=True )
    is_hidden = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_released = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    modified_by = models.IntegerField(null=True)

class Like(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

class Comment(models.Model):
    body =  models.TextField(null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

