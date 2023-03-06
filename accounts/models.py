import datetime
from django.db import models
from django.core.cache import cache
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

import uuid
import json
import random
import string

# User = get_user_model()


class CustomUser(AbstractUser):
    id = models.UUIDField(
        _("User ID"), primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )

    def __str__(self) -> str:
        return self.email


class Location(models.Model):
    id = models.UUIDField(
        _("Location ID"),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    name = models.CharField(_("Location"), max_length=50)

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    id = models.UUIDField(
        _("Profile ID"),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    user = models.OneToOneField(
        CustomUser, verbose_name=_("User"), on_delete=models.CASCADE
    )
    first_name = models.CharField(_("First Name"), max_length=50)
    middle_name = models.CharField(_("Middle Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    birth_date = models.DateField(
        _("Birth Date"),
        blank=True,
        null=True,
    )
    phone = models.CharField(_("Phone"), max_length=50)
    address = models.TextField(_("Address"))
    location = models.ForeignKey(
        Location,
        verbose_name=_("Location"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self) -> str:
        return f"{self.user.username}"

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        cache.set(f"profile_{self.user_id}", self)

    @classmethod
    def get_cached_profile(cls, user_id):
        profile = cache.get(f"profile_{user_id}")
        if profile is None:
            profile = cls.objects.get(user_id=user_id)
            cache.set(f"profile_{user_id}", profile)
        return profile

    def delete(self, *args, **kwargs):
        self.clear_cache()
        super().delete(*args, **kwargs)

    def clear_cache(self):
        cache.delete(f"profile_{self.user_id}")

    def to_json(self):
        return json.dumps(
            {
                "id": self.id,
                "user_id": self.user_id,
                "first_name": self.first_name,
                "middle_name": self.middle_name,
                "last_name": self.last_name,
                "birth_date": self.birth_date.isoformat() if self.birth_date else None,
                "phone": self.phone,
                "address": self.address,
            }
        )

    @classmethod
    def from_json(cls, data) -> dict:
        profile_dict = json.loads(data)
        profile = cls(user_id=profile_dict["user_id"])
        profile.first_name = profile_dict["first_name"]
        profile.middle_name = profile_dict["middle_name"]
        profile.last_name = profile_dict["last_name"]
        profile.phone = profile_dict["phone"]
        profile.address = profile_dict["address"]
        if profile_dict["birth_date"]:
            profile.birth_date = datetime.datetime.fromisoformat(
                profile_dict["birth_date"]
            )
        return profile


class Wallet(models.Model):
    id = models.UUIDField(
        _("Wallet ID"),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    user = models.OneToOneField(
        CustomUser, verbose_name=_("User"), on_delete=models.CASCADE
    )
    balance = models.DecimalField(
        _("Balence"), max_digits=10, decimal_places=2, default=0
    )
    updated = models.DateTimeField(_("Updated"), auto_now_add=True)

    class Meta:
        verbose_name = _("Wallet")
        verbose_name_plural = _("Wallets")

    def __str__(self) -> str:
        return f"{self.user.username}"


class ReferralCode(models.Model):
    id = models.UUIDField(
        _("Referral ID"),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )
    user = models.ForeignKey(
        CustomUser, verbose_name=_("User refferal"), on_delete=models.CASCADE
    )
    code = models.CharField(_("Referral Code"), max_length=8)
    email = models.EmailField(_("Invited Email"), max_length=254, blank=True, null=True)
    referred_user = models.ForeignKey(
        CustomUser,
        verbose_name=_("Referred"),
        on_delete=models.CASCADE,
        related_name="referral_referred_user",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Referral Code")
        verbose_name_plural = _("Referral Codes")

    def __str__(self) -> str:
        return f"{self.code}"

    def save(self, *args, **kwargs):
        code = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
        while ReferralCode.objects.filter(code=code).exists():
            code = "".join(random.choice(string.ascii_uppercase + string.digits, k=8))
        self.code = code
        super().save(*args, **kwargs)

    def get_referred_users(self):
        return self.referred_users.all()
