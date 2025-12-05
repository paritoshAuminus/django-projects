from django.contrib import admin
from .models import Student, Class_model, Subjects

# Register your models here.
class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


@admin.register(Class_model)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'full_name', 'section']
    search_fields = ['name', 'section']
    list_display_links = ['name']
    ordering = ['section']
    inlines = [StudentInline]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'father_name', 'class_name', 'roll_no'] 
    list_display_links = ['first_name']
