from django.urls import path

from users.views import UserLoginView, UserRegistrationView, ProfileUserView, logout, follow, EditProfile, ProfileContentView
from users import views
from posts import views


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registr'),
    path('profile/<slug:slug>/', ProfileUserView.as_view(), name='profile'),
    path('profile/edit/<slug:slug>/', EditProfile, name='profile_edit'),
    path('<username>/follow/<option>/', follow, name='follow'),
    path('profile/content/<str:content_type>/', ProfileContentView.as_view(), name='profile-content'),

]