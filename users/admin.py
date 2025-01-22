from django.contrib import admin

from users.models import User
from posts.models import Follow


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    prepopulated_fields = {"slug": ("username",)}

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'following']

