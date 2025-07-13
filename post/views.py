from django.shortcuts import render

# Create your views here.


def index(request):
    name = "KSI"
    return render(request, 'post/home.html', {
        "name": name
    })


def post_detail(request, id):
    return render(request, 'post/post_detail.html', {
        "id": id
    })
