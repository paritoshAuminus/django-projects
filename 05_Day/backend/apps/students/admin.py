from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'class_room')  # FIXED
    search_fields = ('name',)
    list_display_links = ('name',)

    autocomplete_fields = ('class_room',)  # FIXED

    filter_horizontal = ('subjects',)

    list_filter = (
        ('class_room', admin.RelatedOnlyFieldListFilter),  # FIXED
    )
