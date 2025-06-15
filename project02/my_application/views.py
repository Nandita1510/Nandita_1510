from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    msg="<h1> WELCOME TO DJANGO </h1>"
    return HttpResponse(msg)
