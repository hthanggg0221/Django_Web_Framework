from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id = id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all().values()
    myquery = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    template = loader.get_template("template.html")
    context = {
        'mymembers': mymembers,
        'firstname': 'Thang',
        'fruits': ['Apple', 'Banana', 'Cherry'],
        'greeting': 2,
        'day': "Friday",
        'x': ['Apple', 'Banana', 'Cherry'], 
        'y': ['Apple', 'Banana', 'Cherry'],
        'emptytestobject': {},
        'myquery': myquery,
        # 'var1': John,
    }
    return HttpResponse(template.render(context, request))