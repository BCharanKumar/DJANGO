from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def example(request):
    #Here I am taking HttpRequest and I am returning HttpResponse
    return HttpResponse('i am from views')