from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    principal = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("app1:detail", kwargs={"pk": self.pk})
    
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=18)
    school = models.ForeignKey(School,related_name='students', on_delete=models.CASCADE)
        
    def __str__(self):
        return self.name