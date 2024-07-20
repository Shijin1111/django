from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import student
from app1.forms import teacherform,portForm
from app1 import forms
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def base(request):
    return render(request,'app1/base.html')

@login_required
def index(request):
    return render(request,'app1/index.html')

def help(request):
    return render(request,'app1/help.html')

def student_list(request):
    student_list = student.objects.all()
    student_dict = {"student":student_list}
    return render(request,"app1/student_list.html",context=student_dict)

def student_details(request):
    student_list = student.objects.all()
    student_dict = {"student":student_list}
    return render(request,"app1/student_details.html",context=student_dict)

def student_form_view(request):
    if request.method == 'POST':
        form = forms.studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('help') 
    else:
        form = forms.studentform()

    return render(request,'app1/studentform.html',{'form':form})



def register(request):
    registered = False
    t = None
    user = request.user# Initialize t to None
    
    if request.method == "POST":
        teacher_form = teacherform(request.POST)
        portfolio_form = portForm(request.POST,request.FILES)
        
        if teacher_form.is_valid() and portfolio_form.is_valid():
            user = User.objects.create_user(
                username=teacher_form.cleaned_data["username"],
                email=teacher_form.cleaned_data["email"],  # Assuming your form has an email field
                password=teacher_form.cleaned_data["password"]
            )
            
            t = teacher_form.save()
            t.set_password(t.password)
            t.user = user
            t.save()
            
            p = portfolio_form.save(commit=False)
            p.t = t
            
            if 'profile_pic' in request.FILES:
                p.profile_pic = request.FILES['profile_pic']
            
            p.save()
            registered = True
        else:
            # Handle form errors if validation fails
            if t:
                print(t.errors)
            else:
                print("t is not defined")
            print(portfolio_form.errors)
        return redirect(reverse('app1:help')) 
    else:
        teacher_form = teacherform()
        portfolio_form = portForm()
    
    return render(request, 'app1/registration.html', {
        'teacherform': teacher_form,
        'portfolioform': portfolio_form,
        'registered': registered
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('app1:index'))
            else:
                return HttpResponse("account not active")
        else:
            print("login failed")
            print("username:{} and password:{} ".format(username,password))
            return HttpResponse("invalid login credentials supplied")
    else:
        return render(request,'app1/login.html')
    
@login_required         
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app1:index'))