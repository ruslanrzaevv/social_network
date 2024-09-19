from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User, Profile
from posts.models import Post
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
    
# class UserRegistrationView(View):
#     template_name = 'users/registration.html'
#     form_class = UserRegistrationForm

#     def form_valid(self, form):
#         user = form.instance

#         if user:
#             form.save()
#             auth.login(self.request, user)

#         return super().form_valid(form)
    
#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context["form"] = 'form'
#         return context


class ProfileView(View):
    def get(self, request):
        posts = Post.objects.filter(user=request.user)

        context = {
            'posts':posts,
            'profile':request.user.profile  

        }
        return render(request, 'users/profile.html',context)


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'users/edit_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('edit_profile')

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    

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