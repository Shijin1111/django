from django.db import models

# Create your models here.
class student(models.Model):
    sname = models.CharField(max_length=100)
    age = models.IntegerField()