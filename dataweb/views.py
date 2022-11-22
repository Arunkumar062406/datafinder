from django.shortcuts import render


# Create your views here.


def Home(request):
    return render(request,'index.html') 


def About(request):
    return render(request,'about.html') 


def Signup(request):
    return render(request,'contact.html')       

def Pricing(request):
    return render(request,'pricing.html')  