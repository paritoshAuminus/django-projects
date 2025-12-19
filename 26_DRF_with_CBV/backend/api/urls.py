from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('students/', StudentAPI.as_view()),            # for GET (all) and POST
    path('students/<int:pk>', StudentAPI.as_view()),    # for GET (single), PUT, PATCH and DELETE
]
