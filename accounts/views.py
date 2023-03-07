import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.core import serializers
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect

from accounts.models import Profile, Wallet
from allauth.account.views import SignupView
from accounts.forms import ProfileForm
from accounts.tasks import send_referral_email


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = Profile.get_cached_profile(user_id=request.user.id)
        form = ProfileForm(instance=profile)
        return render(request, "accounts/profile.html", {"form": form})

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
        else:
            return render(request, "accounts/profile.html", {"form": form})


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "accounts/profile_detail.html"


class WalletView(LoginRequiredMixin, View):
    def get(self, request):
        wallet = Wallet.objects.get(user=request.user)
        return render(request, "accounts/wallet.html", {"wallet": wallet})


# class CustomSignupView(SignupView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if "ref" in self.request.GET:
#             referral_code = self.request.GET["ref"]
#             try:
#                 referral = ReferralCode.objects.get(code=referral_code)
#                 context["referral"] = referral
#             except ReferralCode.DoesNotExist:
#                 pass
#         return context
