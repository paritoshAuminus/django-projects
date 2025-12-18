from django.db import models

# Create your models here.
class YoutubeUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    subscribers = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    friends = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
