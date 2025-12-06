from django.db import models

# Create your models here.
class Class_model(models.Model):
    class_choices = [
        (None, 'Select Class'),
        ('I', 'First'),
        ('II', 'Second'),
        ('III', 'Third'),
        ('IV', 'Four'),
        ('V', 'Fifth'),
        ('VI', 'Sixth'),
        ('VII', 'Seventh'),
        ('VIII', 'Eighth'),
        ('IX', 'Ninth'),
        ('X', 'Tenth'),
    ]

    section_choices = [
        (None, 'Select Section'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    name = models.CharField(max_length=4, choices=class_choices)
    section = models.CharField(max_length=1, choices=section_choices)

    @property
    def full_name(self):
        return self.name

    def __str__(self):
        return f'{self.name} - {self.section}'
    
    class Meta:
        unique_together = ('name', 'section')
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'



class Subjects(models.Model):
    subject_choices = [
        (None, 'Select Subject'),
        ('MATH', 'Mathematics'),
        ('SCI', 'Science'),
        ('ENG', 'English'),
        ('SST', 'Social Studies'),
        ('BIO', 'Biology'),
        ('PHY', 'Physics'),
        ('CHEM', 'Chemistry'),
    ]

    name = models.CharField(max_length=4, choices=subject_choices)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    class_name = models.ForeignKey(Class_model, on_delete=models.CASCADE, related_name='student')
    roll_no = models.PositiveIntegerField()
    subjects = models.ManyToManyField(Subjects, verbose_name=("subjects"), related_name='student')

    def __str__(self):
        return self.first_name