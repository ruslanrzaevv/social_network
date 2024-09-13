from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth

from users.forms import UserLoginForm




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
                return redirect('admin')
            
        return render(request, 'users/login.html', {'form':form})


