from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="post_homepage"),
    path('id/<int:id>/', views.post_detail_by_id, name="post_detail"),
    # path('<str:slug>/', views.post_detail_by_slug, name="post_by_slug")
    path('<str:slug>/', views.PostDetailView.as_view(), name="post_by_slug"),
    path('comment/<int:pk>/edit/',
         views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/',
         views.CommentDeleteView.as_view(), name='comment_delete'),
]
