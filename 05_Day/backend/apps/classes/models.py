from django.db import models
from apps.school.models import School



class Classes(models.Model):
    CLASS_LEVELS = [
        ("NUR", "Nursery"),
        ("KG", "Kindergarten"),
        ("1", "Class 1"),
        ("2", "Class 2"),
        ("3", "Class 3"),
    ]

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="classes"
    )
    grade = models.CharField(max_length=3, choices=CLASS_LEVELS)
    section = models.CharField(max_length=1, default="A")

    class Meta:
        unique_together = ("school", "grade", "section")
        verbose_name = "Class Room"
        verbose_name_plural = "Class Rooms"
        ordering = ["school", "grade", "section"]

    def __str__(self):
        return f"{self.get_grade_display()} - {self.section} ({self.school.name})"
