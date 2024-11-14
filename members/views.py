from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import NewMembers

# Create your views here.
def members(request):
    mymembers=NewMembers.objects.all().values()
    template=loader.get_template('all_members.html')

    context = {
        'mymembers': mymembers,
    }

    return HttpResponse(template.render(context,request))


def details(request,id):
    mymember = NewMembers.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
    

def testing(request):
    mymembers=NewMembers.objects.all().values()
    #mydata=Member.objects.filter(empno='1234').values()
    #mydata=Member.objects.values_list('ename')
    mydata=NewMembers.objects.all().order_by('ename','empno').values()
    
    template=loader.get_template('template.html')
    context = {
        'members':mymembers,
        'emptyobject':[],
        'fruits': ['apple','banana','mango'],
        #'mymembers':mymembers,
        'mymembers':mydata,
        }
    return HttpResponse(template.render(context, request))

def main(request):
    
    template=loader.get_template('main.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))