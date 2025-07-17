from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all().select_related('category')
    return render(request, 'post/home.html', {
        'posts': posts
    })


def post_detail(request, id):
    return render(request, 'post/post_detail.html', {
        "id": id
    })
