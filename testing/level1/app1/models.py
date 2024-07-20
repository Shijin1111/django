from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student(models.Model):
    sname = models.CharField(max_length=100)
    age = models.IntegerField()
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)