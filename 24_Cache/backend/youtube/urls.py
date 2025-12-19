from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('profile/', views.profile_view, name='profile'),
    path('video/', views.video_view, name='video'),
    path('blog/', views.blog_view, name='blog'),
]
