from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import EmployeeMaster

# Create your views here.
def main(request):
    template = loader.get_template('shop40office/main.html')
    context = {
   
    }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('shop40office/index.html')
    context = {
   
    }
    return HttpResponse(template.render(context, request))