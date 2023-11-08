from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jam(request):
    return HttpResponse('<h1><marquee>Hi How R U</h1></marquee>')
