from django.db import models
from django.utils  import timezone
# Create your models here.
from django.db import models
from .manager import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Users(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Others'),
    )
    email = models.CharField(max_length=50, null=False, unique=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    dob = models.DateField(null=True)
    bio = models.CharField(max_length=150, null=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    country = models.CharField(max_length=50, null=True)
    img_profile = models.ImageField(upload_to='uploads/user/', null=True)
    is_artist = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_by = models.IntegerField(null=True)
    img_cover = models.ImageField(upload_to='uploads/user/', null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELD = []

    def __str__(self):  
        return self.email
    

