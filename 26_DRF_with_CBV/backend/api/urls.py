from django.urls import path, include
from .views import StudentAPI, StudentListCreateAPI, StudentRetrieveUpdateDeleteAPI, StudentViewsets
from rest_framework.routers import DefaultRouter

# --------------------------------------------
# urls for StudentAPI
# --------------------------------------------

# urlpatterns = [
#     path('students/', StudentAPI.as_view()),            # for GET (all) and POST
#     path('students/<int:pk>', StudentAPI.as_view()),    # for GET (single), PUT, PATCH and DELETE
# ]


# --------------------------------------------------------------------
# urls for for StudentListCreateAPI and StudentRetrieveUpdateDeleteAPI
# --------------------------------------------------------------------

# urlpatterns = [
#     path('students/', StudentListCreateAPI.as_view()),                   # for GET (all) and POST
#     path('students/<int:pk>', StudentRetrieveUpdateDeleteAPI.as_view()), # for GET (single), PUT, PATCH and DELETE
# ]


# --------------------------------------------------------------------
# urls for for StudentViewsets
# --------------------------------------------------------------------

router = DefaultRouter()
router.register('students', StudentViewsets, basename='students')

urlpatterns = [
    path('', include(router.urls))
]
