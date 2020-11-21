from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contact
# Create your views here.
def home(request):
    x=876789
    return render(request,'index.html',{'x':x})

def about(request):
    return render(request,'about.html')

def contact_page(request):
    return render(request,'contact.html')
def news(request):
    return render(request,'news.html')

def contact_submit(request):
    return render(request,'contact.html')
