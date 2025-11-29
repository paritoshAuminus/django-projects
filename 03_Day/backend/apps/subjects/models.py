# subjects/models.py

from django.db import models

# Create your models here.
class Subject(models.Model):
    ALL_SUBJECTS = [
        ('MATH', 'Mathematics'),
        ('SCI', 'Science'),
        ('GK', 'General Knowledge'),
        ('MSC', 'Moral Science'),
        ('SST', 'Social Studies'),
    ]
    name = models.CharField(max_length=4, choices=ALL_SUBJECTS)

    def __str__(self):
        return self.name
    
