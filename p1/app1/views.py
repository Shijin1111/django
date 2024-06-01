from django.shortcuts import render
from app1.models import User
# Create your views here.

def index(request):
    return render(request,'app1/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = { 'users': user_list }
    return render(request,'app1/users.html',context=user_dict)