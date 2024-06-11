from django.shortcuts import render
from app1.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'app1/index.html')

@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == "POST":
        userform = UserForm(data=request.POST)
        profileform = UserProfileInfoForm(data=request.POST)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            
            profile = profileform.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            
            registered = True
        else:
            print(userform.errors,profileform.errors)
    else:
        userform = UserForm()
        profileform = UserProfileInfoForm()
    
    return render(request,'app1/registration.html',{'userform':userform,
                           'profileform':profileform,
                           'registered':registered})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("account not active")
        else:
            print("someone tried to login anf failed")
            print("username:{} and password:{}",format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'app1/login.html',{})