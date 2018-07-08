from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, CustomUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password',)
