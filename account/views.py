from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import FormView


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = UserCreationForm
    success_url = '/'  # 🔹 Keep it simple and direct students to homepage

    def form_valid(self, form):
        user = form.save()  # Save the user
        login(self.request, user)  # Log the user in
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Logs errors to the terminal
        return super().form_invalid(form)
