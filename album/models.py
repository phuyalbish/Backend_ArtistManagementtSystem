from django.utils import timezone
from django.db import models
from user.models import Users
class Album(models.Model):
    name = models.CharField(max_length=50, null=False)
    description =  models.CharField(max_length=50, null=True)
    img_banner = models.ImageField(upload_to='uploads/album/', null=True)
    img_profile = models.ImageField(upload_to='uploads/album/', null=True)
    artist = models.ForeignKey(Users, default="Anonymous", on_delete=models.SET_DEFAULT)
    created_at = models.DateTimeField(default=timezone.now)
    release_at = models.DateTimeField(default=timezone.now)
    totallike = models.IntegerField(default=0)
    totalmusic = models.IntegerField(default=0)
    is_hidden = models.BooleanField(default=0)
    is_deleted = models.BooleanField(default=0)
    is_released = models.BooleanField(default=0)
    is_disabled = models.BooleanField(default=0)
    modified_by = models.CharField(max_length=50, null=True)



