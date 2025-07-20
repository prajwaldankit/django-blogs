from django.shortcuts import render, redirect
from core.models import Feedback

# Create your views here.


def index(request):
    name = "from the core app"
    return render(request, 'post/home.html', {
        "name": name
    })


def contact(request):
    if (request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST['email']
        message = request.POST['message']
        feedback = Feedback(
            name=name,
            email=email,
            message=message
        )
        feedback.save()
        return redirect("homepage")
    return render(request, 'core/contact.html')


def about_us(request):
    return render(request, 'core/about-us.html')
