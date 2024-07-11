from django.urls import path
from hr import views
urlpatterns = [
    path('hrHome/', views.hrHome,name='hr_home'),
    path('post_job/', views.post_job,name='post_job'),
]