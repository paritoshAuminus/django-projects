from django.contrib import admin
from .models import Patient, VisitingRecords

# Register your models here.
admin.site.register(Patient)
admin.site.register(VisitingRecords)