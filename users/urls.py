from django.urls import path

from users.views import UserLoginView, UserRegistrationView, ProfileView, ProfileUpdateView
from users import views


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('registration/', UserRegistrationView.as_view(), name='registr'),
]
