from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('class_view/', views.class_view, name='class_view'),
    path('student_view/', views.sutdent_view, name='sutdent_view'),
]
