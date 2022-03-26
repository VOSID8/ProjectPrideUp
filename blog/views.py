from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/blogs.html', {
        'posts': posts
    })

def post(request, slug=None):
    post = Post.objects.filter(slug=slug).first
    if post is None:
        return redirect('/blog/')
    return render(request, 'blog/insta.html', {
        'post': post
    })
