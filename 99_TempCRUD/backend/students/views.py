from django.shortcuts import render
from .models import Class_model, Student

# Dashboard >>> List of all classes
def dashboard_view(request):
    class_name = Class_model.objects.all()
    return render(request, 'students/dashboard.html', {'class_name': class_name})

# Class view >>> List of all students inside a class
def class_view(request, pk):
    students = Student.objects.get(class_name=pk)
    return render(request, 'students/class_view.html', {'students': students})

# Student view >>> Information about one student
def student_view(request, pk):
    student = Student.objects.get(pk = pk)
    return render(request, 'students/student_view.html', {'student': student})