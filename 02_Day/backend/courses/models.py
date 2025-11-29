from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0.0)
    description = models.TextField(null=True, blank=True)