from django.shortcuts import render

# Create your views here.


def index(request):
    name = "KSI"
    return render(request, 'post/home.html', {
        "name": name
    })
