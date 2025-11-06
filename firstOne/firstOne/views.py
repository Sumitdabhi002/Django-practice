from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse("Hello, this is new project page home")
  return render(request,'index.html')

def about(request):
  # return HttpResponse("Hello, this is new project page about")
  return render(request,'about.html')

def contact(request):
  return HttpResponse("Hello, this is new project page contact")