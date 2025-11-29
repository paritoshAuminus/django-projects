from django.contrib import admin
from .models import Classes


@admin.register(Classes)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("id", "class_name", "school", "section")
    search_fields = ("grade", "section", "school__name")
    list_filter = ("grade", "section", "school")
    list_display_links = ("class_name",)

    def class_name(self, obj):
        return f"{obj.get_grade_display()} - {obj.section}"
    
    class_name.short_description = "Class Name"
