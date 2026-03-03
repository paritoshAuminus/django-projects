from django.urls import path
from .views import CreateTask, ListTasks, ListTask, UpdateTask

urlpatterns = [
    # view task list, create task, update task, delete task, get task
    path('v1/tasks/create/', CreateTask.as_view()),
    path('v1/tasks/get/', ListTasks.as_view()),
    # path('v1/tasks/<int:pk>/', ListTask.as_view()),
    path('v1/tasks/get/<int:pk>/', ListTask.as_view()),
    path('v1/tasks/update/<int:pk>/', CreateTask.as_view()),
]

