from django.contrib import admin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_name', 'is_optional')
    search_fields = ('name',)

    def display_name(self, obj):
        return obj.get_name_display()
    display_name.short_description = "Subject"
