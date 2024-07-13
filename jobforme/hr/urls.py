from django.urls import path
from hr import views
urlpatterns = [
    path('hrHome/', views.hrHome_view,name='hr_home'),
    path('post_job/', views.post_job_view,name='post_job'),
    path('candidate_details/', views.candidate_view,name='candidate_details'),
]