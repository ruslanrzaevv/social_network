from django.shortcuts import render
from django.views import View

from posts.models import Post
from posts.forms import CommentForm


class MainView(View):
    def get(self, request):

        posts = Post.objects.all()
        form = CommentForm()

        context = {
            'title': 'Главная страница',
            'posts': posts,
            'form': form,
        }
        return render(request, 'main/index.html', context)