from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet, RegisterAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')



urlpatterns = [
    path('', include(router.urls) ),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
