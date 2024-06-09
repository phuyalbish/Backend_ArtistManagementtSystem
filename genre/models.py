from django.db import models

class Genre(models.Model):
    WEATHER = (
    ('Clear', 'Clear'),
    ('Clouds', 'Clouds'),
    ('Rain', 'Rain'),
    ('Drizzle', 'Drizzle'),
    ('Thunderstorm', 'Thunderstorm'),
    ('Snow', 'Snow'),
    ('Mist', 'Mist'),
    ('Smoke', 'Smoke'),
    ('Haze', 'Haze'),
    ('Dust', 'Dust'),
    ('Fog', 'Fog'),
    ('Sand', 'Sand'),
    ('Ash', 'Ash'),
    ('Squall', 'Squall'),
    ('Tornado', 'Tornado'),
    )
    name = models.CharField(max_length=50, null=False, unique=True)
    is_deleted = models.BooleanField(default=False)
    modified_by = models.IntegerField(null=True)
    weather = models.CharField(max_length=20, choices=WEATHER, null=True)

