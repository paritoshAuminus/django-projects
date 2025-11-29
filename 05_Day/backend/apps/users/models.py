# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mobile = models.IntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

