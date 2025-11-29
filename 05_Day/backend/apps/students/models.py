from django.db import models
from apps.classes.models import Classes
from apps.subjects.models import Subject


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_number = models.PositiveIntegerField()
    class_room = models.ForeignKey(
        Classes,
        on_delete=models.CASCADE,
        related_name="students"
    )
    subjects = models.ManyToManyField(
        Subject,
        related_name="students"
    )
    date_of_birth = models.DateField(null=True, blank=True)
    admission_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["class_room", "roll_number"]
        unique_together = ("class_room", "roll_number")
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.name} (Roll {self.roll_number})"
