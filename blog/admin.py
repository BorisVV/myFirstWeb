

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserSignUpForm, UserLoginForm
from .models import Post
from .models import CustomUser

admin.site.register(Post)

class CustomUserAdmin(UserAdmin):
    add_form = UserSignUpForm
    form = UserLoginForm
    model = CustomUser
    list_display = ['username', 'email', 'password',]

admin.site.register(CustomUser, CustomUserAdmin)
