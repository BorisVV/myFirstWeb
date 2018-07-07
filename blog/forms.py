from django import forms

from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class UserSignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
