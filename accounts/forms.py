from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


from accounts.models import CustomUser, Profile, UserLocation


class CustomUserCreationForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "first_name",
            "middle_name",
            "last_name",
            "birth_date",
            "phone",
        )


class UserLocationForm(forms.ModelForm):
    class Meta:
        model = UserLocation
        fields = ("state", "region", "location", "street")
