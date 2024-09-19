from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


from posts.forms import UserPostForm
from posts.models import Post
from posts.forms import CommentForm


class AddPostView(CreateView):

    model = Post
    form_class =UserPostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('index')  
        return render(request, 'includes/include_post.html', {'post': post, 'form': form})
    


