from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


from users.models import User, Profile


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):  
    class Meta:
        model = User  
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)  
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)



class ProfileForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = (
            "user",
            'bio',
            "location",
            "birth_date",
            "image",
            )

    user = forms.CharField(required=False)
    bio = forms.CharField()
    location = forms.CharField()
    birth_date = forms.DateField()
    image = forms.ImageField()


