from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from . import models
# Create your views here.
class indexView(TemplateView):
    template_name = 'app1/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["injectme"] = "THIS IS CONTENT"
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    # if i don't add the above stmt ,then django
    # will give it defaultly as school_list -> which is the lowercase for that model+_list
    model = models.School
    
class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    # this just return modelname in lowercase
    model = models.School
    template_name = 'app1/school_details.html'
    
class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name','principal','location')
    
class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name','principal')
    
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("app1:list")