from django.db import models
from accounts.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500) 
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_blogs')

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments')
    content = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.user} - {self.content}'