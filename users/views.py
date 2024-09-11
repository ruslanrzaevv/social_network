from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth

from users.forms import UserLoginForm




class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'users/login.html', {'form':form})
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST('username')
            password = request.POST('password')

            user = auth.authenticate(username=username, password=password)   
            if user:
                auth.login(request, user)
                return redirect('admin')

