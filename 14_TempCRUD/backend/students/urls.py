from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('class_view/<int:class_id>', views.class_view, name='class_view'),
    path('student_view/<int:student_id>', views.sutdent_view, name='student_view'),
    path('class_view/add/', views.add_student, name='add_student'),
    path('class_view/edit/<int:student_id>', views.edit_student, name='edit_student'),
    path('class_view/delete/<int:student_id>', views.delete_student, name='delete_student'),
]
