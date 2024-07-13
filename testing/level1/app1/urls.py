from django.urls import path
from app1 import views

urlpatterns = [
    path('help/',views.help,name="help"),
    path('slist/',views.student_list,name="slist"),
    path('sdetails/',views.student_details,name="details"),
    path('sform/',views.student_form_view,name="sform"),
]