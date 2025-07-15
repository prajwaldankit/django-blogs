from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="post_homepage"),
    path('<int:id>/', views.post_detail, name="post_detail")
]
