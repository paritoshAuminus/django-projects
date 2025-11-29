from django.urls import path, re_path
from . import views

urlpatterns = [
    path('post/<str:blog_id>', views.blogpost, name='blog_post'),
    path('user/<str:user_id>', views.user_profile, name='user_id'),
    re_path(r"^date/(?P<year>[0-9]{4})/$", views.blog_by_year, name='blog_by_year'),
    path('article/<int:year>/<int:month>', views.article_details, name='article_details'),
    path('home/', views.home_page, name='home_page')
]
