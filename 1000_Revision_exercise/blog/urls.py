from django.urls import path
from .views import BlogList, RetrieveBlog

urlpatterns = [
    path('blogs/', BlogList.as_view()),
    path('blogs/<int:pk>/', RetrieveBlog.as_view()),
]
