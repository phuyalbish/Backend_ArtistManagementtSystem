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
    ASIAN_COUNTRIES = (
    ('Afghanistan', 'Afghanistan'),
    ('Armenia', 'Armenia'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bahrain', 'Bahrain'),
    ('Bangladesh', 'Bangladesh'),
    ('Bhutan', 'Bhutan'),
    ('Brunei', 'Brunei'),
    ('Cambodia', 'Cambodia'),
    ('China', 'China'),
    ('Cyprus', 'Cyprus'),
    ('Georgia', 'Georgia'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Iran', 'Iran'),
    ('Iraq', 'Iraq'),
    ('Israel', 'Israel'),
    ('Japan', 'Japan'),
    ('Jordan', 'Jordan'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Kuwait', 'Kuwait'),
    ('Kyrgyzstan', 'Kyrgyzstan'),
    ('Laos', 'Laos'),
    ('Lebanon', 'Lebanon'),
    ('Malaysia', 'Malaysia'),
    ('Maldives', 'Maldives'),
    ('Mongolia', 'Mongolia'),
    ('Myanmar', 'Myanmar'),
    ('Nepal', 'Nepal'),
    ('Oman', 'Oman'),
    ('Pakistan', 'Pakistan'),
    ('Palestine', 'Palestine'),
    ('Philippines', 'Philippines'),
    ('Qatar', 'Qatar'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Singapore', 'Singapore'),
    ('South Korea', 'South Korea'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Syria', 'Syria'),
    ('Taiwan', 'Taiwan'),
    ('Tajikistan', 'Tajikistan'),
    ('Thailand', 'Thailand'),
    ('Timor-Leste', 'Timor-Leste'),
    ('Turkey', 'Turkey'),
    ('Turkmenistan', 'Turkmenistan'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('Uzbekistan', 'Uzbekistan'),
    ('Vietnam', 'Vietnam'),
    ('Yemen', 'Yemen'),
)

    email = models.CharField(max_length=50, null=False, unique=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    dob = models.DateField(null=True)
    bio = models.CharField(max_length=200, null=True)
    gender = models.IntegerField(choices=GENDER, default=0)
    country = models.CharField(max_length=50, choices=ASIAN_COUNTRIES, null=True)
    img_cover = models.ImageField(upload_to='uploads/user/cover/', null=True, default='uploads/default/cover.jpeg' )
    img_profile = models.ImageField(upload_to='uploads/user/profile/', null=True,   default='uploads/default/defaultUser.jpg' )
    is_artist = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_disabled = models.BooleanField(default=False)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_by = models.IntegerField(null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):  
        return self.email
    

    

