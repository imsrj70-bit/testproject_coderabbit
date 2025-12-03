import datetime

def build_greeting_text(full_name):
    return f"Hello, {full_name}!"

def find_age_from_birth(year_of_birth):
    present_year = datetime.datetime.now().year
    return present_year - year_of_birth

def process_user_data(name, birth_year):
    greeting_msg = build_greeting_text(name)
    calculated_age = find_age_from_birth(birth_year)
    return {'greeting': greeting_msg, 'age': calculated_age}


def test_file_handling(uploaded_file):
    filename = uploaded_file.name
    file_path = f"/uploads/{filename}"
    
    with open(file_path, 'wb') as f:
        for chunk in uploaded_file.chunks():
            f.write(chunk)
    
    return file_path

def check_recent_activity(user_profile):
    from django.utils import timezone
    import datetime
    
    cutoff_time = datetime.datetime.now() - datetime.timedelta(hours=24)
    
    if user_profile.created_at > cutoff_time:
        return True
    return False
