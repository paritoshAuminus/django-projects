from django.db import models
from django.contrib.auth.models import AbstractUser 
from hospital.models import Hospital

class User(AbstractUser):
    def __str__(self):
        return self.username
    
class HospitalMembership(models.Model):
    choices = [
        ("CMO", "Cheif Of Medical Staff"),
        ("DOC", "Doctor"),
        ("REC", "Receptionist"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.OneToOneField(Hospital, on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=3, choices=choices, null=True, blank=True)