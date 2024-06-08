from django.shortcuts import render
from app1.forms import UserForm,UserProfileInfoForm
# Create your views here.
def index(request):
    return render(request,'app1/index.html')

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
