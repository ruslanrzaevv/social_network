from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from posts.forms import UserPostForm
from posts.models import Post

class AddPostView(CreateView):
    model = Post
    form_class =UserPostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
