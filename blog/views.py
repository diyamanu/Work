
from django.shortcuts import render,HttpResponse

# Create your views here.
def welcome(request):
    return render(request,"welcome.html",{})

def Garde(request):
    return render(request,"index.html",{})

def Hour(request):
    return render(request,"Hours.html",{})

def Sub1(request):
    return render(request,"Sub1.html",{})

def Sub(request):
    return render(request,"Time and Date.html",{})