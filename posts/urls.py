from django.urls import path


from posts.views import AddPostView



urlpatterns = [
    path('create-post/', AddPostView.as_view(), name='create_post')
]

