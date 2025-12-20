from django.urls import path
from . import views

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

urlpatterns = [
    path('blog/', views.blog_list, name='blog_list'),
]
