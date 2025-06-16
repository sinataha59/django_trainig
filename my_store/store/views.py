from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request , name):
   
    return render (request,"hello.html",{"name":name})


def say_name(request):
    name = input("enter your name :   ")
    return HttpResponse(name)
def something(request , num):
    print(type(num))
    print(num)
    return HttpResponse('some thing')
