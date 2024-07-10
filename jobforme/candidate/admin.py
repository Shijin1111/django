from django.contrib import admin
from candidate import models
# Register your models here.

@admin.register(models.MyApplyJobList)
class MyApplyJobListAdmin(admin.ModelAdmin):
    list_display = ('id','user','job','dateYouApply')
# or just do
# admin.site.register(MyJobList)

@admin.register(models.isShortList)
class isShortListAdmin(admin.ModelAdmin):
    list_display = ('id','user','job','dateYouApply')

    