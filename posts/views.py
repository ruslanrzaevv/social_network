from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from rest_framework import generics, viewsets
from rest_framework.decorators import action  
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination


from posts.forms import UserPostForm
from posts.models import Post, Likes, Comment
from posts.forms import CommentForm
from posts.serializers import PostSerializer
from posts.permisions import IsAdminOrReadOnly, IsOwnerOrReadOnly


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Post.objects.all()[:3]
#         return Post.objects.filter(pk=pk)
    
#     @action(methods=['GET'], detail=True, basename='post')

#     def comment(request, pk):
#         comment = Comment.objects.get(pk=pk)
#         return Response({'comment': comment.title})
    

class PostApiListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000

class PostApiList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PostApiListPagination

class PostApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostApiDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)





# class PostApiView(APIView):
#     # queryset = Post.objects.all()
#     # serializer_class = PostSerializer
    
#     def get(self, request):
#         p = Post.objects.all()
#         return Response({'posts':PostSerializer(p, many=True).data})

#     def post(self, request):
#         serializer = PostSerializer
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not alowed"})
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

#         serializer = PostSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post':serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"ERROR": "Delete Method Is Not Allowed"})

#         try:
#             instance = Post.objects.get(pk=pk)
#             instance.delete()
#             print('asdfkljasklfja;slkdfjaskljf;alksdjf;asldjfa;lj')
#         except:
#             return Response({"ERROR": "Object Not Found !"})

#         return Response({"post": f"Object {str(pk)} is deleted"})




class AddPostView(CreateView):

    model = Post
    form_class =UserPostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

# class PostDetailView(View):
#     template_name = 'posts/post_detail.html'

#     def get(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         context = {
#             'post': post,
#             'comments': post.comments.all(),  # Предполагается, что у вас есть связь с комментариями
#             'form': CommentForm(),
#         }
#         return render(request, self.template_name, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context= {
        'posts':post,
    }
    return render(request, 'posts/post_detail.html', context)
    

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
    



def like(request, post_slug):
    user = request.user
    post = Post.objects.get(slug =post_slug)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()
    if not liked:
        liked= Likes.objects.create(user=user, post=post)
        current_likes += 1
    else:       
        liked = Likes.objects.filter(user=user, post=post).delete()
        current_likes -= 1

    post.likes = current_likes
    post.save()
    return redirect('post_detail', slug=post_slug)


def reels(request):
    posts = Post.objects.filter(is_video=True)
    return render(request, 'posts/reels.html', {'posts':posts})

def reels_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/reels_det.html', {'post':post})
