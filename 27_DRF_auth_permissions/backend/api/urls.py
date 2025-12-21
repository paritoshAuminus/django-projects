from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

# ------------------------------------------------------------------------
# for Authentication: BasicAuthentication and Permission: IsAuthenticated
# ------------------------------------------------------------------------

# urlpatterns = [
#     path('public/', views.public_view, name='public_view'),
#     path('private/', views.private_view, name='private_view'),
# ]


# ------------------------------------------------------------------------------------
# for Authentication: SessionAuthentication and Permission: IsAuthenticatedOrReadOnly
# ------------------------------------------------------------------------------------

# urlpatterns = [
#     path('blog/', views.blog_list, name='blog_list'),
# ]


# ------------------------------------------------------------------------
# for Authentication: TokenAuthentication and Permission: IsAuthenticated
# ------------------------------------------------------------------------

# urlpatterns = [
#     path('auth-token/', obtain_auth_token, name='api_auth_token'),
#     path('profile/', views.user_profile, name='user_profile'),
#     path('admin/', views.admin_panel, name='admin_panel'),
# ]


# -------------------------------------------------------------------------------
# for Authentication: JWTAuthentication and Permission: IsAuthenticatedOrReadOnly
# -------------------------------------------------------------------------------

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('post_list/', views.post_list, name='post_list'),
]
