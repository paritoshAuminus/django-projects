from django.contrib.auth.models import AbstractUser
from django.db import models
from consultancy.models import Consultancy

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username


class ConsultancyMember(models.Model):
    CHOICES = [
        ('CONSULTANT', 'Consultant'),
        ('STAFF', 'Staff'),
        ('CLIENT', 'Client'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    consultancy = models.ForeignKey(Consultancy, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=CHOICES, default="CLIENT")


