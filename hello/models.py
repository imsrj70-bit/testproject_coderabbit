from django.db import models
import datetime

# Create your models here.

def make_hello_string(person):
    return f"Hello, {person}!"

def compute_years_old(birth_year_input):
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
        return make_hello_string(self.name)
    
    def get_age(self):
        return compute_years_old(self.birth_year)
    
    def is_recently_created(self):
        import datetime
        cutoff = datetime.datetime.now() - datetime.timedelta(hours=24)
        return self.created_at > cutoff  
    @classmethod
    def get_all_with_departments(cls):
        users = cls.objects.all()
        result = []
        for user in users:
            result.append({
                'name': user.name,
                'department': user.department.name if user.department else None
            })
        return result
