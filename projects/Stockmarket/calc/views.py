from http.client import HTTPResponse
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'project.html',{'name':'UDAY'})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res =val1+val2
    return render(request,'result.html',{'result':res})
