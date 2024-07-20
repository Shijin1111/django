Django
project creation:   django-admin startproject project_name
cd to the new project folder to create new app
app creation : python manage.py startapp app_name
run project:  python manage.py runserver    (it works when executed from the folder which have manage.py)
 
URL Calls View Name:
Path('', views.index, name='index')
Views Call Template Name:
Return render(request, 'app1/help.html')
In this case, 'app1' is the directory where the HTML file is located, specifically within templates → app1 → HTML files.

after creating app:
goto app → views and do
from django.http import HttpResponse
create function
def index(request):
return HttpResponse(“hello world”)
goto urls.py
from app1 import views
add path('',views.index,name='index'), in url patters  ( here ‘’ is for pattern matching for url and views.index calls the function from views and name is just given for later use )
goto  settings → installed apps add the app name
run  python manage.py runserver 

url using include

goto project → project’s url.py and add
from django.urls import include
or just add include after path
from django.urls import path,include
“in new version, instead of url it uses path.You can see this in import path and also in below of that .there we use path instead of url”
Now inside the urlpatterns add 
path('appname/',include('appname.urls')),
Create urls.py file in appfolder and add
from django.urls import path
from appname import views

urlpatterns = [
    path('',views.index,name='index'),
]

templates
create a directory named templates and under that create directories in the name of appnames and under this appdirectories you can add html files.
goto project → settings.py 
pathlib module is used in settings.py for ensuring platform independence.it creates the path accessible for other machines also by giving it a common name  BASE_DIR. So BASE_DIR acts as the root of the file system and pathlib is used to create paths in this file system.
from pathlib import Path
now we can create a path for templates by doing,
TEMPLATES_DIR = BASE_DIR/"templates"
and under that, in templates give
'DIRS': [TEMPLATES_DIR],
goto templates → appname →  something.html 
use {{ some variable }} which is a template tag
goto appname → views and inside the function add
mydict={ ’some variable’ : “put something here” }
under that add
    return render(request,'index.html',context=my_dict)
so the views will look like this,
def welcome(request):
    my_dict = { 'insert_me':'hello am i from views.py' }
    return render(request,'app1/index.html',context=my_dict)
render: This is a helper function provided by Django that combines a template with a context dictionary to produce a complete HTML page.
request:represents the HttpRequest object that Django passes to your view function when handling a request from a client. This object contains information about the request made by the client, including details such as GET and POST parameters, headers, user information (if authenticated), and more.
'app1/index.html': ‘templates/’  is not required becuase it’s specified in templates dictionary.This is the path to the template file that you want to render. The path is relative to the directories listed in the DIRS option of your TEMPLATES setting in your Django settings file.
context=my_dict: This is a dictionary of context data that you want to pass to the template. The keys in this dictionary become the context variables in the template.

In Django, you don't directly call or invoke HTML template files from your code. Instead, you set up views that render these templates and pass context data to them. This approach is a fundamental part of the Model-View-Template (MVT) architecture that Django follows. 
“so we call the views, and in the return render function the second parameter is the template”

Static files
create a directory static and inside that another directory images
goto project → project → settings.py and STATIC_DIR = BASE_DIR/"static"  
just like we did for templates.
in the end of the file add
STATICFILES_DIRS = [
    STATIC_DIR,
]
now in index.html add this, 
<!DOCTYPE html>
{% load static %}
and in body add this
<img src="{% static "images/justimage.jpg" %}" alt="oh oh didn't show">
use <link rel="stylesheet" href="static/css/first.css" > to use css.
until this is recaped in 126.Introduction to Django Level Two
   

models
goto app → models and create models(models are tables in django) like this,
class Topic(models.Model):
    topic_name=models.CharField(max_length=264,unique=True)
    
    def __str__(self):
        return self.topic_name
after this
makemigrations:
Creates migration files based on changes in your models.
Does not alter the database directly.
Generates Python files in the migrations directory.
migrate:
Applies migration files to the database.
Updates the database schema according to the instructions in the migration files.
python manage.py migrate
python manage.py makemigrations appname
and again do migrate.
python manage.py migrate (this is beacause you created new migration files and this have to be updated in database)

to create admin do 
python manage.py create superuser
to register models with admins do this
from appname.models import Topic,AccessRecord,Webpage
admin.site.register(Topic)


faker
faker is used to populate your database with fake data.This can be useful in testing and all.
create a populate_appname.py file in project directory
add following
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'project_name.settings')

import django
django.setup()

import random
from faker import Faker
from appname.models import Topic,Webpage,AccessRecord
create a Faker object
fake = Faker()     OR        fakegen = Faker()
create a function to populate data
def populate(N=5)
for i in range(N):
fake_name = fakegen.company()
      acc_rec = AccessRecord.objects.get_or_create(name=fake_name)[0]

 

MTV
goto views and do following,
import models from appname/models 
add this also
def welcome(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'accessrecords':webpages_list}
    return render(request,'appname/index.html',context=date_dict)

lecture video 132 is a recap for everything till now.

Forms
define form just like models
in views import forms
forms.Form1() initializes an instance of the form Form1 defined in the forms.py file within the app2 application.
{'form': form} is the context dictionary. It contains data that you want to make available in the template. In this case, it contains a single key-value pair where the key is 'form' and the value is the form instance.
create templates 
add urls
form validation
we can use a botcatcher element to catch bots.
just add     botcatcher = forms.CharField(required=False,widget=forms.HiddenInput) 
in form elements.and put a function in forms.py itself.
def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if(len(botcatcher)>0):
            raise forms.ValidationError("gotcha bottt!")
        return botcatcher
we can look at form validation while doing projects.
ModelForm
A ModelForm in Django is a class that automatically creates a form based on a Django model. It is a powerful feature that allows you to easily create forms for your database models without having to manually define each field in the form.
1.Define a Model: First, define a model in your models.py file.
from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name
2.Create a ModelForm: Next, create a ModelForm for the Person model in your forms.py file.
from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta://M in caps.
        model = Person
        fields = ['name', 'email', 'birth_date']


template inheritance
template filters
https://chatgpt.com/share/a395ddad-1fa2-4b03-8549-c9f286007987
recap till now in lecture 141.

If you ran the python3 -m venv myenv command in your home directory (/home/yourusername), the path to your virtual environment would be:
/home/yourusername/myenv

CBV
import this: 
from django.views.generic import View
and add a class in view,
and also in the urls.py you cannot call the view because there is no view ,so call the class with .as_view method.
https://chatgpt.com/share/b39867d1-0065-4372-ab09-e8cc857b160c
including media files
media  : pip install pillow
in form tag of the template ,
<form method="POST" enctype="multipart/form-data">

*args allows you to pass a variable number of non-keyword arguments to a function.
**kwargs allows you to pass a variable number of keyword arguments to a function.
class based views
First you should read below and then gpt
https://chatgpt.com/share/9b771c1a-b39e-42e4-84d1-504f1f26b130
There is no classnameview class.we have to make template or list or deails or ‘something’view class and we have to pick the best fit class based view.
if you want to just showcase your template then use templateView.If you want to list or print details of a model then use listView.but if you want to print the details of a specific object then you have to use detailView.If you have to create new object for a model then use createView.
in urls.py add it as     path('index/',views.CBView.as_view(),name="index"),
here instead of views.index we called views.classname.as_view()

class SchoolListView(ListView):
    context_object_name = 'students'
    # if i don't add the above stmt ,then django
    # will give it defaultly as studentlist -> which is the lowercase for that model+list
    model = models.School
templateView
create view as below:
from django.views.generic import TemplateView  
class HomePageView(TemplateView): 
template_name = 'home.html'

and now add url as:
path('', TemplateView.as_view(template_name='home.html'), name='home'),
actually for templateView, we only have to call:
TemplateView.as_view(template_name='home.html').this will use the home.html.no need for view.
When you want to add content to the home.html you can add 
def get_context_data(self, **kwargs):
context = super().get_context_data(**kwargs) 
context['welcome_message'] = 'Welcome to the Home Page!' 
return context
in the views.
So the templateView will look like this:

if you do this on your models.py as a def of a model then when we update or delete or create with that model then this absolute_url will work to redirect to a page we specified.
def get_absolute_url(self):
        return reverse("app1:detail", kwargs={"pk": self.pk})

