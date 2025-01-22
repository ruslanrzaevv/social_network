from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    image = models.ImageField(default='users.image',upload_to='users_image', blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug and self.username:
            self.slug = slugify(self.username)  # self здесь это сам объект User
        super().save(*args, **kwargs)

    
class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pciture", null=True, default="default.jpg")
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True) 


    def save(self,  *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username   
    

