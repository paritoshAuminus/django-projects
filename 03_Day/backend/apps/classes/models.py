# classes/models.py

from django.db import models

# Create your models here.
class Classes(models.Model):
    ALL_CLASSES = [
        ('NU', 'nursery'),
        ('KG', 'kindergarten'),
        ('1A', '1A'),
        ('1B', '1B'),
        ('2A', '2A'),
        ('2B', '2B'),
        ('3A', '3A')
    ]
    class_name = models.CharField(max_length=2, choices=ALL_CLASSES)

    def __str__(self):
        return self.class_name
