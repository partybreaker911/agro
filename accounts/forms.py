from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm

from accounts.models import CustomUser, Profile


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
            "address",
        )


class ReferralForm(forms.Form):
    email = forms.EmailField(
        required=False,
    )


class ReferralSignupForm(SignupForm):
    referral_code = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["placeholder"] = "Email Address"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["referral_code"].widget.attrs["placeholder"] = "Referral Code"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm password"

    def save(self, request):
        user = super().save(request)
        referral_code = self.cleaned_data.get("referral_code")
        if referral_code:
            try:
                code = ReferralCode.objects.get(code=referral_code)
            except ReferralCode.DoesNotExist:
                code = None

            if code and not ReferralCode.objects.filter(user=user, code=code).exists():
                ReferralCode.objects.create(
                    user=user, code=code, referred_by=code.referred_by
                )

        return user
