from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
class CBView(View):
    def get(self,request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL.RIGHT?")