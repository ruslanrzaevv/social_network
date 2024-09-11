from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True, null=True, )
    phone_number = models.CharField(max_length=15, unique=True)
