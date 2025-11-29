from django.db import models


class Subject(models.Model):
    SUBJECTS = [
        ("MATH", "Mathematics"),
        ("SCI", "Science"),
        ("ENG", "English"),
        ("SST", "Social Studies"),
    ]

    name = models.CharField(max_length=10, choices=SUBJECTS)
    is_optional = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.get_name_display()
