from django.shortcuts import render
from .models import Category

# Create your views here.


def index(request):
    categories = Category.objects.all()
    return render(request, 'category/home.html', {
        "categories": categories
    })
