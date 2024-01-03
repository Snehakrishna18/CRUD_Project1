from django.db import models

# Create your models here.

class EmployeeDetails(models.Model):
    YOUR_CHOICES = [
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
    ]
    name = models.CharField(max_length = 20)
    mobile_num = models.IntegerField()
    email = models.EmailField()
    position = models.CharField(max_length = 30, choices=YOUR_CHOICES)
    