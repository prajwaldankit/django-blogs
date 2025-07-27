from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_index, name="api_home"),
    path('posts/', views.get_all_posts, name="posts_get_api"),
]
