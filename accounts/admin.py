from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser, Profile, Wallet, Location
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


class ProfileAdmin(admin.ModelAdmin):
    model = admin
    list_display = [
        "id",
        "user",
        "first_name",
        "middle_name",
    ]


admin.site.register(Profile, ProfileAdmin)

admin.site.register(Wallet)

admin.site.register(Location)
