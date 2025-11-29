from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=254, unique=True)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name