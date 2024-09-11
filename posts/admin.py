from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'content', 'created_at']
    prepopulated_fields = {"slug": ("title",)}
