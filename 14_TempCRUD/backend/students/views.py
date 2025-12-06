from django.shortcuts import render, get_object_or_404, redirect
from .models import Class_model, Student, Subjects

# Create your views here.
# List of all classes
def dashboard(request):
    class_name = Class_model.objects.all()
    return render(request, 'students/dashboard.html', {'class_name': class_name})

# List of all students inside one class
def class_view(request, class_id):
    class_obj = get_object_or_404(Class_model, id=class_id)    # Get one class students not all of em
    students = Student.objects.filter(class_name = class_obj)
    return render(request, 'students/student_list.html', {'students': students, 'class_obj': class_obj})

# One student
def sutdent_view(request, student_id):
    student = Student.objects.get(id = student_id)     # Get one student not all students
    subjects = student.subjects.all()
    return render(request, 'students/student.html', {'student': student, 'subjects': subjects})

# Add a new student
def add_student(request):
    class_name = Class_model.objects.all()
    subjects = Subjects.objects.all()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        roll_no = request.POST.get('roll_no')
        
        class_id = request.POST.get('class_name')
        class_obj = Class_model.objects.get(id=class_id)

        subject_ids = request.POST.getlist('subjects')
        subject_objs = Subjects.objects.filter(id__in=subject_ids)


        # creating new student
        student = Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            father_name = father_name,
            roll_no = roll_no,
            class_name = class_obj,
        )

        student.subjects.set(subject_objs)
        return redirect('dashboard')

    return render(request, 'students/add_student.html', {'class_name': class_name, 'subjects': subjects})

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)

    all_class_names = Class_model.objects.all()
    selected_class_name = student.class_name
    all_subjects = Subjects.objects.all()
    student_subjects = student.subjects.all()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        roll_no = request.POST.get('roll_no')
        class_name = request.POST.get('class_name')
        subjects = request.POST.getlist('subjects')

        student.first_name = first_name
        student.last_name = last_name
        student.father_name = father_name
        student.roll_no = roll_no
        student.class_name_id = class_name  # better than .get(...)
        student.subjects.set(subjects)

        student.save()  # or use update_fields=["first_name", "last_name", "father_name", "roll_no", "class_name"]

        return redirect('sutdent_view', student.id)

    return render(
        request,
        'students/edit_student.html',
        {
            'student': student,
            'all_class_names': all_class_names,
            'selected_class_name': selected_class_name,
            'all_subjects': all_subjects,
            'student_subjects': student_subjects,
        }
    )

def delete_student(request, student_id):

    if request.method == 'POST':
        student_to_delete = Student.objects.get(id=student_id)
        student_to_delete.delete()
        return redirect('dashboard')

    return render(request, 'students/delete_student.html', {'student_id': student_id})
