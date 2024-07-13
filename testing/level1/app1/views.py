from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import student
from app1 import forms
# Create your views here.
def index(request):
    return HttpResponse("<em>hello shijin</em>")

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