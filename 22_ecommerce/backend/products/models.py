from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE, related_name='product')
    stock = models.IntegerField()
    
    def __str__(self):
        return self.name