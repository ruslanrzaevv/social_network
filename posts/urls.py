from django.urls import path


from posts.views import AddPostView, AddCommentView,post_detail, like, reels, reels_detail



urlpatterns = [
    path('create-post/', AddPostView.as_view(), name='create_post'),
    path('post-detail/<slug:slug>/', post_detail, name='post_detail'),
    path('add-comment/<int:post_id>/', AddCommentView.as_view(), name='add_comment'),
    path('<slug:post_slug>/like/', like, name='like'),
    path('reel/', reels, name='reel'),
    path('reels/<slug:slug>/', reels_detail, name='reels_det'),
]


