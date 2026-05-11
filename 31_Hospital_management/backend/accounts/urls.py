from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import get_user, register

urlpatterns = [
    path("login/v1/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/v1/", TokenRefreshView.as_view(), name="refresh"),
    path("register/v1/", register, name="register"),
    path("getuser/v1/", get_user, name="get_user"),
]

