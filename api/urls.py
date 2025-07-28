from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_index, name="api_home"),
    path('posts/', views.ListPosts.as_view(), name="posts_get_api"),
    path('posts/<slug:slug>/', views.PostDetail.as_view(),
         name='post_by_slug_api'),
    path('posts/<slug:slug>/comments', views.get_comments_for_post_by_slug,
         name='comment_post_by_slug'),
    path('comments/', views.get_all_comments, name="all_comments_api"),
]
