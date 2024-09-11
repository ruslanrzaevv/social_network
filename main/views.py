from django.shortcuts import render
from django.views import View

from posts.models import Post


class MainView(View):
    def get(self, request):

        posts = Post.objects.all()

        context = {
            'title': 'Главная страница',
            'posts': posts
        }
        return render(request, 'main/index.html', context)