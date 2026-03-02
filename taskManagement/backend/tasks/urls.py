from django.urls import path
from .views import CreateTask

urlpatterns = [
    # view task list, create task, update task, delete task, get task
    path('v1/tasks/create', CreateTask.as_view()),
    path('v1/tasks/', CreateTask.as_view()),
    path('v1/tasks/<int:pk>/', CreateTask.as_view()),
    # path('v1/tasks/create', CreateTask.as_view()),
]

