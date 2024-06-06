from django.shortcuts import render
#from app1.models import User
from app1.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'app1/index.html')

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form =NewUserForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return index(request)
    else:
        print("error")
    return render(request,'app1/users.html',{'form':form})

        