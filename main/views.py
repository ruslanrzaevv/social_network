from django.shortcuts import render
from django.views import View
from django.db.models import Q


from posts.models import Post
from posts.forms import CommentForm
from users.models import User
from main.mixins import RekomendationMixin

class MainView(View, RekomendationMixin):
    def get(self, request):
        query = request.GET.get('q', '')
        posts = Post.objects.all().order_by('-created_at')
        form = CommentForm()
        users= User.objects.all()

        if query:
            users = User.objects.filter(
                Q(username__icontains=query) |  
                Q(first_name__icontains=query) | 
                Q(last_name__icontains=query)
            )

        rec_posts = self.rekomendation(request.user)

        context = {
            'title': 'Главная страница',
            'posts': rec_posts,
            'h':posts,
            'form': form,
            'users':users,
            'query':query,
        }
        return render(request, 'main/index.html', context)
    
    
