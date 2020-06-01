from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name' ,'username', 'email']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Your Email')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['ProfilePic']