from django.urls import path


from posts.views import AddPostView, AddCommentView



urlpatterns = [
    path('create-post/', AddPostView.as_view(), name='create_post'),
    path('add-comment/<int:post_id>/', AddCommentView.as_view(), name='add_comment')
]

