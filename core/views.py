from django.shortcuts import render, redirect
from django.views import View
from core.models import Feedback

# Create your views here.


def index(request):
    name = "from the core app"
    return render(request, 'post/home.html', {
        "name": name
    })


class ContactView(View):
    template_name = 'core/contact.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Feedback.objects.create(
            name=name,
            email=email,
            message=message
        )
        return redirect("homepage")


# def contact(request):
#     if (request.method == "POST"):
#         name = request.POST.get('name')
#         email = request.POST['email']
#         message = request.POST['message']
#         feedback = Feedback(
#             name=name,
#             email=email,
#             message=message
#         )
#         feedback.save()
#         return redirect("homepage")
#     return render(request, 'core/contact.html')
#
#

def about_us(request):
    return render(request, 'core/about-us.html')
