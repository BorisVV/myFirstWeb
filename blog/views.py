
from django.shortcuts import \
        render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm, UserSignUpForm, UserLoginForm
from django.contrib import messages
from .models import Post, CustomUser

# Create your views here

def login(request):
    return render(request, 'blog/login.html', {'success': 'Success!'})

def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'post': post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_name = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_name = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

# def login(request):
#     if request.method == 'POST':
#         user_signIn_form = UserLoginForm(request.POST)
#         if user_signIn_form.is_valid():
#             user_signIn_form.save()
#             messages.success(request, 'You have signed in succesfully!')
#             return redirect('blog/post_detail')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         user_signIn_form = UserLoginForm()
#     return render(request, 'blog/login.html', {'user_signIn_form': user_signIn_form})


def logout(request):
    pass

def sign_up(request):
    if request.method == 'POST':
        user_signUp_form = UserSignUpForm(request.POST)
        if user_signUp_form.is_valid():
            user_signUp_form.save()
            messages.success(request, 'Sign Up completed!!!')
            return redirect('blog/post_detail')
        # else:
        #     messages.error(request, 'Please correct the error.')
    else:
        user_signUp_form = UserSignUpForm()
    return render(request, 'blog/sign_up.html', {'user_signUp_form': user_signUp_form})
