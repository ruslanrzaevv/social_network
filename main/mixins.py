from django.db.models import Q

from posts.models import Post, Follow

class RekomendationMixin:
    def rekomendation(self, user):

        if user.is_authenticated:
            followwing_users = Follow.objects.filter(follower=user).values_list('following', flat=True)
            recommended_posts = Post.objects.filter(
                Q(user__in=followwing_users)
            ).exclude(user=user).order_by('-created_at')
        else:
            recommended_posts = Post.objects.all().order_by('-created_at')[:10] 
            
        return recommended_posts