from django.contrib import admin
from .models import User, HospitalMembership

# Register your models here.
admin.site.register(User)
admin.site.register(HospitalMembership)