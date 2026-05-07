from django.db import models
from hospital.models import Hospital
from accounts.models import User
import uuid
from accounts.models import HospitalMembership
from django.core.exceptions import ValidationError

# Patient records model - User -> FK -> Patient
class Patient(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="patient_record", null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_identified = models.BooleanField(default=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.hospital}'

# Visiting date - Patient -> FK -> VisitingRecords
class VisitingRecords(models.Model):
    choices = [
        ("SC", "Scheduled"),
        ("VS", "Visited"),
        ("NS", "No-Show"),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    scheduled_date = models.DateField()

    status = models.CharField(max_length=2, choices=choices, default="SC")
    doctor = models.ForeignKey(HospitalMembership, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.user.username

    def clean(self):
        if self.doctor.role != "DOC":
            raise ValidationError("Selected hospital member is not a doctor")
        
        if self.doctor.hospital != self.patient.hospital:
            raise ValidationError("Doctor and patient must belong to the same hospital")


