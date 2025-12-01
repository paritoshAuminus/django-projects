from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Task)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'complete', 'created_at')
    list_filter = ('complete', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)