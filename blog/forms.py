from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Post, CustomUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password',)

class UserLoginForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password',)
