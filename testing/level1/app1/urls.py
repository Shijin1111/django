from django.urls import path
from app1 import views

app_name = 'app1' 

urlpatterns = [
    path('help/',views.help,name="help"),
    path('slist/',views.student_list,name="slist"),
    path('sdetails/',views.student_details,name="details"),
    path('sform/',views.student_form_view,name="sform"),
    path('index/',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name="user_login"),
]