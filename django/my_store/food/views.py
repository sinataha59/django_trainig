from django.shortcuts import render
from django.http import HttpResponse

def food_waiter(request,name):
    return HttpResponse(f"your order is {name}")

def drink_waiter(request):
    return HttpResponse("your order is soda")
