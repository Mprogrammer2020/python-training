from django.db import models

# Create your models here.

class Student(models.model):
    name =models.CharField(max_length=100)
    college =models.CharField(max_length=100)
    city =models.CharField(max_length=100)