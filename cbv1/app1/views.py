from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    
    #  we can either specify template_name here.if we didn't then django will use --AI mechanism to 
    # find the best match template. here it took school_list bcz we already used 'schools' in 
    # that template.
        
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'app1/school_details.html'
    