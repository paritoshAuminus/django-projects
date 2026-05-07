from django.db import models
from django.contrib.auth.models import AbstractUser 
from hospital.models import Hospital, Department
from django.core.exceptions import ValidationError


# User model
class User(AbstractUser):
    def __str__(self):
        return self.username
    
# HospitalMembership - User -> FK -> HospitalMembership + Hospital -> FK -> HospitalMembership
class HospitalMembership(models.Model):
    choices = [
        ("CMO", "Chief Of Medical Staff"),
        ("DOC", "Doctor"),
        ("REC", "Receptionist"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hospital_membership")
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    role = models.CharField(max_length=3, choices=choices)

    def __str__(self):
        return f'{self.user.username} - {self.role}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=["hospital"],
            condition=models.Q(role="CMO"),
            name="unique_cmo_per_hospital"
            ),

            models.UniqueConstraint(
                fields=["hospital", "user"],
                name="unique_user_hospital_membership"
            )
        ]

class DepartmentMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="department_membership")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.role}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "department"],
                name="unique_user_per_department"
            )
        ]
