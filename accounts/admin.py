from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser, Profile, Wallet, ReferralCode, Location
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
    ]


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Profile)

admin.site.register(Wallet)


class ReferralCodeAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "code",
    ]


admin.site.register(ReferralCode, ReferralCodeAdmin)


admin.site.register(Location)
