
from django.urls import path
from . import  views
urlpatterns = [
  path('hello/<name>/',views.say_hello) , 
  path('hello/',views.say_hello) , 
  path('name/', views.say_name) ,
  path('something/<int:num>/',views.something)
]
