from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from core.models import Feedback
from core.forms import FeedbackForm

# Create your views here.


def index(request):
    name = "from the core app"
    return render(request, 'post/home.html', {
        "name": name
    })


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def about_us(request):
    return render(request, 'core/about-us.html')
