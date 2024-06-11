from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy
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
    
class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School
    
class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School
    
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('app1:list')