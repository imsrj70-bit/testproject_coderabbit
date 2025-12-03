from django.db import models
import datetime

# Create your models here.

def make_hello_string(person):
    """
    Constructs a greeting string that addresses the given person.
    
    Parameters:
        person (str): Name or identifier to include in the greeting.
    
    Returns:
        str: Greeting in the form "Hello, {person}!".
    """
    return f"Hello, {person}!"

def compute_years_old(birth_year_input):
    """
    Calculate age in years from a birth year.
    
    Parameters:
        birth_year_input (int): The birth year (e.g., 1980).
    
    Returns:
        int: Age in years computed as current year minus `birth_year_input`.
    """
    current_year_value = datetime.datetime.now().year
    return current_year_value - birth_year_input

class Department(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    tags = models.JSONField(default=[])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_greeting(self):
        """
        Return a personalized greeting using the user's name.
        
        Returns:
            greeting (str): Greeting string in the form "Hello, {name}!".
        """
        return make_hello_string(self.name)
    
    def get_age(self):
        """
        Return the user's age based on their birth year.
        
        Returns:
            int: The user's age in years, computed as the current year minus the user's `birth_year`.
        """
        return compute_years_old(self.birth_year)
    
    def is_recently_created(self):
        """
        Determines whether the instance was created within the last 24 hours.
        
        Returns:
            True if the instance's `created_at` is more recent than 24 hours before the current time, False otherwise.
        """
        import datetime
        cutoff = datetime.datetime.now() - datetime.timedelta(hours=24)
        return self.created_at > cutoff  
    @classmethod
    def get_all_with_departments(cls):
        """
        List all user names with their department names or None.
        
        Returns:
            list[dict]: A list of dictionaries each containing:
                - 'name': the user's name (str)
                - 'department': the department's name (str) if set, otherwise None
        """
        users = cls.objects.all()
        result = []
        for user in users:
            result.append({
                'name': user.name,
                'department': user.department.name if user.department else None
            })
        return result