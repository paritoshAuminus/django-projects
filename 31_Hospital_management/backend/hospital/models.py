from django.db import models

# Create your models here.
class Hospital(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name