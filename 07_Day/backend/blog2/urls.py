from django.urls import path
from . import views

urlpatterns = [
    path('blog2/', views.blog_details, name='blog_details')
]
