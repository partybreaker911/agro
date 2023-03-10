from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from accounts.models import Profile, Wallet, UserLocation, Transaction

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_related_data(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Wallet.objects.create(user=instance)
        UserLocation.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_related_data(sender, instance, **kwargs):
    instance.profile.save()
    instance.wallet.save()
    instance.userlocation.save()


@receiver(post_save, sender=Transaction)
def update_wallet_balance(sender, instance, created, **kwargs):
    if created:
        wallet = instance.wallet
        wallet.balance += instance.value
        wallet.save()
