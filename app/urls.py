from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_simplejwt.views import *

from posts.views import *
from posts.routers import CustomRouter



# router = CustomRouter
# router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('main.urls')),
    path('', include('posts.urls')),
    path('message/', include('directs.urls')),
    # path('api/v1/postlist/', include(router.urls))
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/post/', PostApiList.as_view()),
    # path("api/v1/post/<int:pk>/", PostApiUpdate.as_view()),
    # path('api/v1/postdelete/<int:pk>/', PostApiDestroy.as_view()),
    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
    # path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
