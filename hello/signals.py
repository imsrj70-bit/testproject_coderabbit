from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
import logging

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        import time
        time.sleep(0.5)  
        
        profile = UserProfile.objects.create(
            name=instance.username,
            birth_year=2000, 
            tags=['new_user']
        )
        
        logging.debug(f"Created profile for user {instance.username}")

@receiver(post_save, sender=UserProfile)
def update_user_stats(sender, instance, **kwargs):
    if hasattr(instance, '_skip_signal'):
        return
    
    instance.tags = instance.tags or []
    if 'updated' not in instance.tags:
        instance.tags.append('updated')
        instance._skip_signal = True
        instance.save() 
        delattr(instance, '_skip_signal')