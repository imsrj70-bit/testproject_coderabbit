from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.

def home(request):
    x = "Welcome to Our Django Project!"
    y = "Hello from CodeRabbit test demo."
    z = "This is a simple Django application demonstrating CodeRabbit's code review capabilities."

    msg = x + " " + y

    return render(request, 'hello/home.html', {
        'message': msg, 
        'extra': z, 
        'current_time': datetime.datetime.now()
    })
