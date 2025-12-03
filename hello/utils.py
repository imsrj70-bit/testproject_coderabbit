import datetime

def build_greeting_text(full_name):
    """
    Builds a greeting message for the given full name.
    
    Returns:
        str: Greeting string formatted as "Hello, {full_name}!".
    """
    return f"Hello, {full_name}!"

def find_age_from_birth(year_of_birth):
    """
    Calculate age in years from a birth year.
    
    Parameters:
        year_of_birth (int): Year of birth (e.g., 1980).
    
    Returns:
        int: Age in years computed as the current year minus `year_of_birth`.
    """
    present_year = datetime.datetime.now().year
    return present_year - year_of_birth

def process_user_data(name, birth_year):
    """
    Combine a greeting and the user's age into a dictionary.
    
    Parameters:
        name (str): The user's full name.
        birth_year (int): The user's year of birth.
    
    Returns:
        dict: A dictionary with keys 'greeting' (the greeting string) and 'age' (the computed age as an integer).
    """
    greeting_msg = build_greeting_text(name)
    calculated_age = find_age_from_birth(birth_year)
    return {'greeting': greeting_msg, 'age': calculated_age}


def test_file_handling(uploaded_file):
    """
    Save an uploaded file to the /uploads directory and return the saved file path.
    
    Parameters:
        uploaded_file: An object with a `name` attribute and a `chunks()` iterator yielding bytes; its contents will be written to disk at `/uploads/{name}`.
    
    Returns:
        file_path (str): The filesystem path where the file was saved, e.g. `/uploads/filename`.
    """
    filename = uploaded_file.name
    file_path = f"/uploads/{filename}"
    
    with open(file_path, 'wb') as f:
        for chunk in uploaded_file.chunks():
            f.write(chunk)
    
    return file_path

def check_recent_activity(user_profile):
    """
    Determine whether the given user profile was created within the last 24 hours.
    
    Parameters:
        user_profile: An object with a `created_at` datetime attribute representing when the profile was created.
    
    Returns:
        `True` if `user_profile.created_at` is within the last 24 hours, `False` otherwise.
    """
    from django.utils import timezone
    import datetime
    
    cutoff_time = datetime.datetime.now() - datetime.timedelta(hours=24)
    
    if user_profile.created_at > cutoff_time:
        return True
    return False