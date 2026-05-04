from django.db import models

# Create your models here.
class Consultancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=None, null=True, blank=True)
    