from django.urls import path
from appname import views

urlpatterns = [
    path('',views.welcome,name='welcome'),
]
