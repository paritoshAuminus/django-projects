from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import GetUser, register

urlpatterns = [
    path('v1/login/', TokenObtainPairView.as_view()),
    path('v1/refresh/', TokenRefreshView.as_view()),
    path('v1/register/', register),
    path('v1/getuser/', GetUser.as_view()),
]



