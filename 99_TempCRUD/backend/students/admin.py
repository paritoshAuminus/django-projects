from django.contrib import admin
from .models import Class_model

# Register your models here.
@admin.register(Class_model)
class Class_admin(admin.ModelAdmin):
    list_display = ['full_name', 'roman', 'section']
    list_display_links = ['full_name']
    search_fields = ['name', 'section']
    ordering = ['name', 'section']

    def roman(self, obj):
        return obj.name  # raw stored value

    roman.short_description = "Name"
