from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from accounts.models import Profile, Wallet, UserLocation

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_wallet(sender, instance, **kwargs):
    instance.wallet.save()


@receiver(post_save, sender=User)
def create_user_location(sender, instance, created, **kwargs):
    if created:
        UserLocation.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_location(sender, instance, **kwargs):
    instance.userlocation.save()
