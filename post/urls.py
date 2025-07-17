from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="post_homepage"),
    path('id/<int:id>/', views.post_detail_by_id, name="post_detail"),
    path('<str:slug>/', views.post_detail_by_slug, name="post_by_slug")
]
