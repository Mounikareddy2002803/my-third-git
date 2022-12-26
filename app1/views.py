from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mouni(request):
    return HttpResponse('<i>app run successfully</i>')

def pys(request):
    return HttpResponse('<b>python is easy to learn</b>' )