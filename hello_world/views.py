from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello! I am Dhiraj Shinde from T3 and my PRN is 1841047<h1>") 