from django.shortcuts import render
from django.http import HttpResponse
from appname.models import Topic,Webpage,AccessRecord
# Create your views here.

def index(Request):
    return HttpResponse("hello worlddddd")

def welcome(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'accessrecords':webpages_list}
    return render(request,'index.html',context=date_dict)
