from django.shortcuts import render
from . import models

# Create your views here.
def student_list(request):
    students = models.Student.objects.all()
    return render(request, 'portfolio/student_list.html', {'students': students})