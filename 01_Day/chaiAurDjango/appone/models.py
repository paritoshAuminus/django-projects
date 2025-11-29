from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CUISINE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='appone/')
    dateAdded = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CUISINE_CHOICE)
    description = models.TextField(default='')
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    

# HANDLING RELATIONAL DATABASE
# One to many
class ChaiReview(models.Model):
    RATING_CHOICE = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    chai = models.ForeignKey(ChaiVariety, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=RATING_CHOICE)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
# many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_variety = models.ManyToManyField(ChaiVariety, related_name='store')

    def __str__(self):
        return self.name

# One to One 
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.chai}'
    
