import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.core import serializers
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect

from accounts.models import Profile, Wallet, ReferralCode
from allauth.account.views import SignupView
from accounts.forms import ProfileForm, ReferralForm
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


class WalletView(LoginRequiredMixin, View):
    def get(self, request):
        wallet = Wallet.objects.get(user=request.user)
        return render(request, "accounts/wallet.html", {"wallet": wallet})


class ReferralLinkView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        referral_code = get_random_string(length=8)
        referrer = self.request.user
        referral = ReferralCode.objects.create(user=request.user, code=referral_code)
        referral_url = request.build_absolute_uri(
            reverse_lazy("account_signup") + "?ref=" + referral_code
        )
        return render(request, "accounts/referral.html", {"referral_url": referral_url})


class CustomSignupView(SignupView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "ref" in self.request.GET:
            referral_code = self.request.GET["ref"]
            try:
                referral = ReferralCode.objects.get(code=referral_code)
                context["referral"] = referral
            except ReferralCode.DoesNotExist:
                pass
        return context


class ReferralInviteView(LoginRequiredMixin, FormView):
    form_class = ReferralForm
    template_name = "accounts/referral_form.html"
    success_url = reverse_lazy("referral_invite")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        token = get_random_string(length=8)
        invite = ReferralCode(user=self.request.user, email=email, code=token)
        invite.save()
        send_referral_email(self.request, invite.user.email)
        messages.success(self.request, "Referral invite send!")
        return JsonResponse({"status": "success"})

    def form_invalid(self, form):
        errors = form.errors.as_json()
        return JsonResponse({"status": "error", "errors": errors})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["referral_invites"] = serializers.serialize(
            "json", ReferralCode.objects.filter(user=self.request.user)
        )
        return context


# class ReferralCodeView(LoginRequiredMixin, TemplateView):
#     template_name = "accounts/referral.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         referral_code = ReferralCode.objects.filter(user=user).first()

#         if not referral_code:
#             pass
#             # code = uuid.uuid4().hex[:8]
#             # referral_code = ReferralCode.objects.create(user=user, code=code)

#         referral_url = self.request.build_absolute_uri(
#             reverse_lazy("account_signup") + f"?code={referral_code.code}"
#         )

#         context["referral_url"] = referral_url
#         return context

#     def post(self, request, *args, **kwargs):
#         email = request.POST["email"]
#         referral_code = ReferralCode.objects.filter(user=request.user).first()
#         referral_url = self.request.build_absolute_uri(
#             reverse_lazy("account_signup") + f"?code={referral_code.code}"
#         )

#         send_referral_email.delay(email, referral_url)

#         return super().post(request, *args, **kwargs)


class ReferralTreeView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/referral_tree.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = self.request.GET.get("code")
        if code:
            users = ReferralCode.objects.get_referred_users(code)
            context["referred_users"] = users
        return context
