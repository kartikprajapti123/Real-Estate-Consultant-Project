from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def service(request):
    return render(request,"service.html")

def contact(request):
    return render(request,"contact.html")

def about_us(request):
    return render(request,"about.html")
