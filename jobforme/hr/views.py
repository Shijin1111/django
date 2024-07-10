from django.shortcuts import render

# Create your views here.
def hrHome(request):
    context = {}
    return render(request,'hr/hrHome.html',context)