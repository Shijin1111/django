from django.urls import path
from hr import views
urlpatterns = [
    path('hrHome/', views.hrHome,name='hr_home'),
]