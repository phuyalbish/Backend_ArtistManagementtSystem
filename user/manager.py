from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        if not password:
            raise ValueError('Password is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)
    


    def create_staff(self, email, password, **kwargs):
            if not email:
                raise ValueError("Email is required")
            if not password:
                raise ValueError('Password is Required')
            
            kwargs.setdefault("is_staff", True)
            user = self.model(email=email, **kwargs)
            user.set_password(password)
            user.save()
            return user

    def getAdmin(self):
            try:
                    res = super().get_queryset().filter(is_staff=True).filter(is_deleted=False, is_disabled=False)
            except:
                return "No Data Found"
            return res



    def create_artist(self, email, password=None, **other_fields):
        other_fields.setdefault("is_artist", True)
        other_fields.setdefault("is_active", True)

        return self.create_user(email, password, **other_fields)
    
    def getArtist(self):
        try:
            res = super().get_queryset().filter(is_artist=True).filter(is_deleted=False, is_disabled=False)
        except:
            return "No Data Found"
        return res


        # aasdasd