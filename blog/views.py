from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post, Category
# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})




def about_page(request):
    return render(request, 'about.html')




def category_detail(request, url):
    cat = get_object_or_404(Category, url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, 'category.html', {'cat': cat, 'posts': posts})



@login_required
def add_post(request, category_url):
    category = get_object_or_404(Category, url=category_url)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.cat = category
            post.author = request.user  # Set the author to the current user
            post.save()
            return redirect('category_detail', url=category_url)
    else:
        form = PostForm(initial={'cat': category})
    return render(request, 'add_post.html', {'form': form, 'category': category})

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        messages.error(request, "You are not allowed to update this post.")
        return redirect('home')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('category_detail', url=post.cat.url)
    else:
        form = PostForm(instance=post)
    return render(request, 'update_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        # Render the template with a flag for unauthorized access
        return render(request, 'delete_post.html', {'post': post, 'unauthorized': True})
    if request.method == 'POST':
        post.delete()
        return redirect('category_detail', url=post.cat.url)
    return render(request, 'delete_post.html', {'post': post})






def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('home')