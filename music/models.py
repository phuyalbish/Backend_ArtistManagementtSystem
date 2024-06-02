from django.utils import timezone 
from django.db import models
from genre.models import Genre
from album.models import Album
from band.models import Band
from user.models import Users

class Music(models.Model):
    name = models.CharField(max_length=50, null=False)
    description =  models.CharField(max_length=150, null=False)
    img_profile = models.ImageField(upload_to='uploads/music/', null=True)
    language = models.CharField(max_length=50, null=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(Users, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)
    release_at = models.DateTimeField(default=timezone.now)
<<<<<<< HEAD
    music_file = models.FileField( upload_to =  'uploads/', null=True )
=======
    music_file = models.FileField( upload_to =  'uploads/music/', null=True )
>>>>>>> 1b4e5c6 (add permission for album, music, and user)
    is_hidden = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_released = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
<<<<<<< HEAD
    modified_by = models.IntegerField(null=True)

class Like(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

class Comment(models.Model):
    body =  models.CharField(max_length=150, null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
=======
    modified_by = models.CharField(max_length=50, null=True)
>>>>>>> 1b4e5c6 (add permission for album, music, and user)

