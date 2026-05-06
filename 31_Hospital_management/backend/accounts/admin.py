from django.contrib import admin
from .models import User, HospitalMembership, DepartmentMembership

# Register your models here.
admin.site.register(User)
admin.site.register(HospitalMembership)
admin.site.register(DepartmentMembership)