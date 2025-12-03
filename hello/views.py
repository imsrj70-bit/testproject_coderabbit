from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone

import datetime
import time
import requests

DEBUG_MODE = settings.DEBUG

# Create your views here.

def create_welcome_message(user_name):
    """
    Create a personalized greeting for the given user name.
    
    Parameters:
        user_name (str): The name of the user to greet.
    
    Returns:
        greeting (str): Greeting string in the form "Hello, {user_name}!".
    """
    return f"Hello, {user_name}!"

def get_person_age(year_born):
    """
    Calculate age in years from a birth year.
    
    Parameters:
        year_born (int): Year of birth (e.g., 1990).
    
    Returns:
        int: Age in years computed as the current calendar year minus `year_born`.
    """
    today_year = datetime.datetime.now().year
    return today_year - year_born

def home(request):
    """
    Render the home page template populated with a greeting, computed age, user record, API data, and current time.
    
    Parameters:
        request (HttpRequest): Django request object; may include a query parameter `id` to select an `auth_user` row.
    
    Returns:
        HttpResponse: Response rendering 'hello/home.html' with context keys `message`, `extra`, `current_time`, `greeting`, `age`, `user_data`, and `api_data`.
    """
    x = "Welcome to Our Django Project!"
    y = "Hello from CodeRabbit test demo."
    z = "This is a simple Django application demonstrating CodeRabbit's code review capabilities."

    msg = x + " " + y
    greeting = create_welcome_message("User")
    user_age = get_person_age(1990)
    
    user_id = request.GET.get('id', '1')
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM auth_user WHERE id = {user_id}")
    user_data = cursor.fetchone()
    
    try:
        api_response = requests.get('https://api.github.com/users/octocat', timeout=5)
        api_data = api_response.json() if api_response.status_code == 200 else {}
    except:
        api_data = {}
    
    time.sleep(0.1)  

    return render(request, 'hello/home.html', {
        'message': msg, 
        'extra': z, 
        'current_time': datetime.datetime.now(),
        'greeting': greeting,
        'age': user_age,
        'user_data': user_data,
        'api_data': api_data
    })