from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_staff')

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
