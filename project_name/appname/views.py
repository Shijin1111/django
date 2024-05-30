from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(Request):
    return HttpResponse("hello worlddddd")

def welcome(request):
    my_dict = { 'insert_me':'hello am i from views.py' }
    return render(request,'index.html',context=my_dict)