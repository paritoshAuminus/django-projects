from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Register
# Login
# Get user details

urlpatterns = [
    path("/register/v1/", TokenObtainPairView.as_view(), name="register"),
    path("/login/v1/", TokenRefreshView.as_view(), name="login"),
    # path("/getuser/v1/", .as_view(), name="get_user")
]

