from django.db import models
from django.contrib.auth.models import User
from hr.models import CandidateApplication,JobPost
# Create your models here.
class MyApplyJobList(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    job = models.ForeignKey(to=CandidateApplication,on_delete=models.CASCADE)
    dateYouApply = models.DateField(auto_now_add=True)
    
class isShortList(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    job = models.OneToOneField(to=JobPost,on_delete=models.CASCADE)
    dateYouApply =  models.DateField(auto_now_add=True)
