from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    path('class_list/<int:pk>', views.class_view, name='class_view'),
    path('student/<int:pk>', views.student_view, name='student_view'),
]
