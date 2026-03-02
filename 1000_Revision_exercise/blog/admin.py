from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published']
    list_filter = ['title', 'author']


admin.site.register(Comment)

