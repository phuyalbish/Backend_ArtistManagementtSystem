from django.contrib import admin
from .models import Music, Like, Comment

admin.site.register(Music, Like, Comment)
