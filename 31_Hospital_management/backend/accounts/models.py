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

# Department Membership - User -> FK -> Department + User -> FK -> Hospital
class DepartmentMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="department_membership")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    # To check whether the department belongs to the same hospital
    def clean(self):
        if self.hospital != self.department.hospital:
            raise ValidationError("The department doesn't belong to the hospital.")

    def __str__(self):
        return f'{self.user.first_name or "First_name"} - {self.department.title}'
    
    # To run the full clean before saving manually
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "department"],
                name="unique_user_per_department"
            )
        ]
