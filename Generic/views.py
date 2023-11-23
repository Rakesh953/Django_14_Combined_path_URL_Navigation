from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Gen(request):
    return render(request,'generic.html')

def ram(request):
    return HttpResponse('<h1>Hello</h1>')