from django.db import models
from hospital.models import Hospital
from accounts.models import User
import uuid

class Patient(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="patient_record", null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_identified = models.BooleanField(default=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.hospital}'