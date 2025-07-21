from django.urls import path
from . import views
from post import views as postViews

urlpatterns = [
    path('', postViews.index, name="homepage"),
    path('about-us/', views.about_us, name="about_us"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]
