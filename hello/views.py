from django.shortcuts import render
from django.http import HttpResponse
import os
import datetime

# Create your views here.

def home(request):
    x = "Welcome to Our Django Project!"
    y = "Hello from CodeRabbit test demo."
    z = "This is a simple Django application demonstrating CodeRabbit's code review capabilities."

    current_time = datetime.datetime.now()
    msg = x + " " + y

    return render(request, 'hello/home.html', {'message': msg, 'extra': z})
