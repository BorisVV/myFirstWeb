

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserSignUpForm, UserLoginForm
from .models import Post, User

admin.site.register(Post)

class CustomUserAdmin(UserAdmin):
    add_form = UserSignUpForm
    form = UserLoginForm
    model = User
    list_display = ['email'] 

admin.site.register(User, CustomUserAdmin)
