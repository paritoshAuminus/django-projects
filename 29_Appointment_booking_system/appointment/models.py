from django.db import models
from consultancy.models import Consultancy

# Create your models here.
class Appointment(models.Model):
    consultancy = models.ForeignKey(Consultancy, on_delete=models.CASCADE)
    

