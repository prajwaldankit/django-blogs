from django.shortcuts import render

# Create your views here.


def index(request):
    name = "from the core app"
    return render(request, 'post/home.html', {
        "name": name
    })


def contact(request):
    return render(request, 'core/contact.html')


def about_us(request):
    return render(request, 'core/about-us.html')
