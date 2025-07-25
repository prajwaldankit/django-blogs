from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',
         LoginView.as_view(template_name='account/login.html',
                           next_page="homepage"),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
