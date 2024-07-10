from django.contrib import admin
from hr import models
# Register your models here.

@admin.register(models.Hr)
class HrAdminAdmin(admin.ModelAdmin):
    list_display = ('id','user')

@admin.register(models.JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id','title','address','companyName','salaryLow','salaryHigh','applyCount','lastDateToApply')

@admin.register(models.CandidateApplication)
class CandidateApplicationAdmin(admin.ModelAdmin):
    list_display = ('id','user','job')

@admin.register(models.SelectCandidateJob)
class SelectCandidateJobAdmin(admin.ModelAdmin):
    list_display = ('id','job','candidate')
