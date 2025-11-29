# students/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    class_name = models.ForeignKey("classes.Classes", on_delete=models.CASCADE, related_name="students")
    subjects = models.ManyToManyField("subjects.Subject", related_name="students")

    def __str__(self):
        return self.name
