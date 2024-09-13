from django.db import models
from users.models import User

class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(null=True,default=None, blank=True, unique=True)
    image = models.ImageField(default='posts.image',upload_to='posts/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
