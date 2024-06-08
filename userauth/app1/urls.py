from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('register',views.register,name="register"),
]
