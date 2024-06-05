from django.shortcuts import render
from app2 import forms
# Create your views here.

def index(request):
    return render(request,'app2/index.html')

def form_name_view(request):
    form = forms.Form1()
    if request.method=='POST':
        form = forms.Form1(request.POST)
        if form.is_valid():
            print("validation success")
            print('name:',form.cleaned_data['name'])
            print('email',form.cleaned_data['email'])
            print('text',form.cleaned_data['text'])
    return render(request,'app2/formpage.html',{'form':form})
