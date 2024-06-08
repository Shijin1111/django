from django.shortcuts import render

# Create your views here.
def index(request):
    dict1 = {'text':'hello world','number':1000}
    return render(request,'basic_app/index.html',dict1)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/rel_url_templates.html')


