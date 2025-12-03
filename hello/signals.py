from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
import logging

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a UserProfile for a newly created User.
    
    When invoked after a User save, if the User was just created this function waits briefly (~0.5s) and then creates a UserProfile with name set to the User's username, birth_year set to 2000, and tags initialized to ['new_user'].
    
    Parameters:
        instance (User): The User instance that was saved.
        created (bool): True when the User instance was created (not just updated).
    """
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
    """
    Ensure a saved UserProfile has the 'updated' tag and persist the change if necessary.
    
    If the instance lacks the 'updated' tag, this function appends 'updated' to instance.tags and saves the instance. It sets a temporary _skip_signal attribute to avoid re-entering signal handlers during the save.
    
    Parameters:
        sender: The model class that sent the signal.
        instance: The UserProfile instance being saved; its `tags` list may be modified and persisted.
        **kwargs: Additional signal keyword arguments (ignored).
    """
    if hasattr(instance, '_skip_signal'):
        return
    
    instance.tags = instance.tags or []
    if 'updated' not in instance.tags:
        instance.tags.append('updated')
        instance._skip_signal = True
        instance.save() 
        delattr(instance, '_skip_signal')