from django.utils import timezone 
from django.db import models
from genre.models import Genre
from album.models import Album
from band.models import Band
from user.models import Users
from customizeable.models import CustomTheme
class Music(models.Model):
    
    name = models.CharField(max_length=50, null=False)
    description =  models.TextField(null=False)
    img_cover = models.ImageField(upload_to='uploads/music/cover/', null=True, default='uploads/default/cover.jpeg' )
    img_profile = models.ImageField(upload_to='uploads/music/profile/', null=True,   default='uploads/default/defaultMusic.jpg' )
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
    theme = models.ForeignKey(CustomTheme, null=True, on_delete=models.SET_NULL)

class Like(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,  related_name='music_like_user')
    is_like = models.BooleanField(default=True)
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='music_likes')

class Comment(models.Model):
    body =  models.TextField(null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,  related_name='music_comment_user')
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='music_comments')
    created_at = models.DateTimeField(default=timezone.now)

class CommentLike(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,   related_name='music_comment_like_user')
    is_like = models.BooleanField(default=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='music_comment_likes')

class CommentReply(models.Model):
    body = models.TextField(null=False)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,   related_name='music_comment_reply_user')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='music_comment_replies')
    created_at = models.DateTimeField(default=timezone.now)

class CommentReplyLike(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,  related_name='music_comment_reply_like_user')
    is_like = models.BooleanField(default=True)
    comment = models.ForeignKey(CommentReply, on_delete=models.CASCADE, related_name='music_comment_reply_likes')