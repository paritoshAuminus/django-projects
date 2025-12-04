from django.db import models

# Create your models here.
class Class_model(models.Model):
    class_choices = [
        (None, 'Select Class'),
        ('I', 'First'),
        ('II', 'Second'),
        ('III', 'Third'),
        ('IV', 'Fourth'),
        ('V', 'Fifth'),
        ('VI', 'Sixth'),
        ('VII', 'Seventh'),
        ('VIII', 'Eighth'),
        ('IX', 'Ninth'),
        ('X', 'Tenth'),
        ('XI', 'Eleventh'),
        ('XII', 'Twelth'),
    ]

    section_choices = [
        (None, 'Select Section'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]

    name = models.CharField(max_length=4, choices=class_choices)
    section = models.CharField(max_length=1, choices=section_choices)

    @property
    def full_name(self):
        return self.get_name_display()


    # def __str__(self):
    #     return self.name
    
    class Meta:
        unique_together = ('name', 'section')

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    class_name = models.ForeignKey(Class_model, on_delete=models.CASCADE, related_name='student')
    roll_no = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name