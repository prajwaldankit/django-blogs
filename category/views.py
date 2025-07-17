from django.shortcuts import render, get_object_or_404
from .models import Category
from post.models import Post

# Create your views here.


def index(request):
    categories = Category.objects.all()
    return render(request, 'category/home.html', {
        "categories": categories
    })


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).select_related('category')

    return render(request, 'category/category_detail.html', {
        'category': category,
        'posts': posts,
    })
