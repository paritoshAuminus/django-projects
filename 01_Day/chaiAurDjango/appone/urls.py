from django.urls import path
from . import views

urlpatterns = [
    path('', views.appone, name='appone'),
    path('<int:food_id>/', views.foodDetails, name='foodDetails')
]