from django.urls import path 
from . import views
urlpatterns = [
    path('food/<name>/',views.food_waiter),
    path('drink/',views.drink_waiter),
]
