from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dj(request):
    return HttpResponse('<h5><marquee>program run without errors</marquee></h5>')

def spider(request):
    return HttpResponse('<h4>SPIDER</h4>')