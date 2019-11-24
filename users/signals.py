# Django Signals help with communicating between apps with DB and components
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Get signal and provide some task
from django.dispatch import receiver
from .models import Profile


# If user is Save came receiver and send signal and get in function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # If exist added
    if created:
        Profile.objects.create(user=instance)

# Check who owns the Post
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Instance is User
    instance.profile.save()
