from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile
"""
 Receives the signal, this is to create a user profile, so we use a receiver decorator. It takes the signal (post_save), when user is saved signal is fired and 
the receiver catches
"""
@receiver(post_save, sender=User) # When something has been saved do something (post_save), Whe are imporing our built-in user model
def create_profile(sender, instance, created, **kwargs):
    if created:
        obj, created = UserProfile.objects.get_or_create(user=instance)