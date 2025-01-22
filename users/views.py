from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib import auth
from django.urls import reverse
from django.db import transaction
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse


from users.forms import UserLoginForm, UserRegistrationForm
from posts.models import Post, Follow,Stream
from users.models import Profile, User
from users.forms import ProfileForm


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'users/login.html', {'form':form})
    
    def post(self, request):
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password=password)   
            if user:
                auth.login(request, user)
                return redirect('index')
            
        return render(request, 'users/login.html', {'form':form})



class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        auth.login(self.request, user)  
        return response

    
    
def logout(request):
    auth.logout(request)
    return redirect('index')

class ProfileUserView(TemplateView):
    template_name = 'users/profile.html'

    def get(self, request, slug):
        user = get_object_or_404(User, slug=slug)
        profile = Profile.objects.filter(user=user)
        posts = Post.objects.filter(user=user)
        count_post = Post.objects.filter(user=user).count()
        following_count = Follow.objects.filter(following=user).count()
        followers_count = Follow.objects.filter(follower=user).count()
        follow_status = Follow.objects.filter(following=user, follower=request.user).exists()
        following_users = User.objects.filter(follower__follower=user)
        followers_users = Follow.objects.filter(following__following=user)


        context = {
            'posts': posts,
            'profile_user': user,  
            'profile':profile,
            'count_post': count_post,
            'following_count': following_count,
            'followers_count': followers_count,
            'follow_status': follow_status,
            'following_users':following_users,
            'followers_users':followers_users,
        }
        return render(request, self.template_name, context)




# class UpdateProfileView(UpdateView):
#     template_name = 'users/update_profile.html'
#     form_class = ProfileForm

#     def get_object(self, queryset=None):
#         try:
#             return Profile.objects.get(slug=self.kwargs['slug'])
#         except Profile.DoesNotExist:
#             user = User.objects.get(slug=self.kwargs['slug'])
#             return Profile.objects.create(user=user, slug=user.slug)


#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
    
#     def form_invalid(self, form):
#         return super().form_invalid(form)
    


#     def get_success_url(self):
#         return reverse('profile', kwargs={'slug': self.object.user.slug})




def EditProfile(request, slug):
    user = request.user.slug
    print(f'username:{user}')
    profile, created = Profile.objects.get_or_create(user__slug=slug, defaults={'user':request.user})

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.image = form.cleaned_data.get('image')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.bio = form.cleaned_data.get('bio')
            print(profile.image, profile.first_name, profile.last_name, profile.location, profile.bio)
            profile.save()
            print(profile)

            
            return redirect('profile', profile.user.username)
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'users/update_profile.html', context)





def follow(request, username, option):
    user = request.user
    following = get_object_or_404(User, username=username)

    try:
        f, created = Follow.objects.get_or_create(follower=request.user, following=following)

        if int(option) == 0:
            f.delete()
            Stream.objects.filter(following=following, user=request.user).all().delete()
        else:
            posts = Post.objects.all().filter(user=following)[:25]
            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post, user=request.user, date=post.created_at, following=following)
                    stream.save()
        return HttpResponseRedirect(reverse('profile', args=[username]))

    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('profile', args=[username]))
    

class ProfileContentView(View):
    def get(self, request, content_type):
        user = request.user  # Текущий пользователь
        content = ""

        if content_type == "posts":
            posts = Post.objects.filter(user=user)
            content = render(request, 'users/content_posts.html', {'posts': posts}).content.decode('utf-8')
        elif content_type == "followers":
            followers = Follow.objects.filter(following=user)
            content = render(request, 'users/content_followers.html', {'followers': followers}).content.decode('utf-8')
        elif content_type == "following":
            following = Follow.objects.filter(follower=user)
            content = render(request, 'users/content_following.html', {'following': following}).content.decode('utf-8')

        return JsonResponse({'html': content})