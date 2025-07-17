from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="categories_home"),
    path('<str:slug>/', views.category_details, name="category_by_slug")
]
