from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import FormView
from django.urls import reverse_lazy


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # Save the user
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Logs errors to the terminal
        return super().form_invalid(form)
