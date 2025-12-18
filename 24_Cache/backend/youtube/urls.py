from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('profile/', views.profile_view, name='profile'),
]
