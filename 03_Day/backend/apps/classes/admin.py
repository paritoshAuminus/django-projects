from django.contrib import admin
from .models import Classes


@admin.register(Classes)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name')
    list_display_links = ('class_name',)
    search_fields = ("class_name",)
