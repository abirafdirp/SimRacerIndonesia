from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, UserProfile


@receiver(signal=post_save, sender=User, dispatch_uid='ensure_profile_exist')
def ensure_profile_exists(sender, instance, **kwargs):
    UserProfile.objects.get_or_create(user=instance)
