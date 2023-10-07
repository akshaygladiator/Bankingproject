#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def index(request):
#    return  HttpResponse("Hello , how are you ? ")

def index(request):

    return  render(request,"Index.html")


def login(request):
    return