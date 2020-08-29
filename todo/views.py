from django.shortcuts import render, HttpResponse


# Create your views here.
def say_hello(request):
    # takes a request from the user and returns the http response
    return HttpResponse("Hello!")
