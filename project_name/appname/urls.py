from django.urls import path
from appname import views

urlpatterns = [
    path('',views.index,name='index'),
]
