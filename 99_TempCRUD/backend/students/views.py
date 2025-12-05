from django.shortcuts import render, get_object_or_404
from .models import Class_model, Student

# Create your views here.
# List of all classes
def dashboard(request):
    class_name = Class_model.objects.all()
    return render(request, 'students/dashboard.html', {'class_name': class_name})

# List of all students inside one class
def class_view(request):
    class_obj = get_object_or_404(Class_model)    # Get one class students not all of em
    students = Student.objects.filter(class_name = class_obj)
    return render(request, 'students/student_list.html', {'students': students, 'class_obj': class_obj})

# One student
def sutdent_view(request):
    student = Student.objects.all()     # Get one student not all students
    return render(request, 'students/student.html', {'student': student})
