from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'class_name')
    search_fields = ('name',)
    list_filter = ('class_name',)
    list_display_links = ('name',)
    filter_horizontal = ("subjects",)      # use for ManyToManyField
    autocomplete_fields = ("class_name",)  # use for ForeignKey