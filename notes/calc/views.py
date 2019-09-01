from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'karan'})

def add(request):
    v1 = int(request.GET["n1"])
    v2 = int(request.GET["n2"])
    res = v1+v2
    return render(request,'result.html',{'result':res})
    