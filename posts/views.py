from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'posts/index.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post' : post,
    }
    return render(request, 'posts/detail.html', context)


def new(request):
    form = PostForm()
    context = {
        'form' : form,
    }
    return render(request, 'posts/new.html')


def create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save()
        return redirect('posts:detail', post.pk)
    context = {
        'form' : form,
    }
    return render(request, 'posts/new.html', context)


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(instance=post)
    context = {
        'post' : post,
        'form' : form,
    }
    return render(request, 'posts/edit.html', context)


def update(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:detail', post.pk)
    context = {
        'form' : form,
    }
    return render(request, 'posts/edit.html', context)