from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView, name='post_list'),
    path('post/', views.PostDetailView, name='post_detail'),
    path('post/create/', views.PostCreateView, name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView, name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView, name='post_delete'),
]
