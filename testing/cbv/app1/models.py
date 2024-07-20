from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("app1:detail", kwargs={"pk": self.pk})
    

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    School = models.ForeignKey("app1.School",on_delete=models.CASCADE,related_name="students")
    def __str__(self):
        return self.name