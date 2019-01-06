
from django.shortcuts import \
        render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import PostForm, UserSignUpForm, UserLoginForm
from .models import Post, User

# Create your views here

def home(request):
    return render(request, 'blog/home.html')

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_name = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, 'Message saved!!')
            return redirect('post_new')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_name = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, 'Post "' + post.title + '" was updated succesfully!!')
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        messages.success(request, 'You have signed in succesfully!')
        return redirect('home')
    else:
        # Return an 'invalid login' error message.
        messages.error(request, 'Please correct the error below.')
    return render(request, 'registration/login.html')

def logout(request):
    auth_logout(request, 'blog/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserSignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def testing_JQuery(request):
    return render(request, 'blog/testingJQuery.html')

def test_JQuery2(request):
    return render(request, 'blog/testJQuery2.html')

def learn_css(request):
    return render(request, 'blog/practiceLearningCSS.html')

def practice_CSS2(request):
    return render(request, 'blog/practiceCSS2.html')
