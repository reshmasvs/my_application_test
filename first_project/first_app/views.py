from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict1 = {'insert_me':"Now I am coming from first_app/index.py"}
    return render(request,'first_app/index.html',context=my_dict1)

def help(request):
    helpdict = {'help_insert':"Help Page"}
    return render(request,'first_app/help.html',context=helpdict)