from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, It's me Kristina!")

def greet(request):
    return HttpResponse("Nice to meet you")

def indexs(request):
    return render(request, "hello/index.html")

def callname(request, name):
    # return HttpResponse(f"Hello, {name}")
    return HttpResponse(f"Hello, {name.capitalize()}!")

