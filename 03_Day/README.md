 ## Stuff in `admin.py`

```bash
 from django.contrib import admin
 from .models import Course

 class CourseAdmin(admin.ModelAdmin):
     search_fields = ('title',)
     list_display = ('title', 'price')
     list_filter = ('price',)
     list_editable = ('price',)

admin.site.register(Course, CourseAdmin)
```