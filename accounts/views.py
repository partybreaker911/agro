from django.contrib import messages
from django.views.generic import (
    View,
    DetailView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from accounts.models import Profile, Wallet, UserLocation, Transaction
from deals.models import Deal
from accounts.forms import ProfileForm, UserLocationForm

User = get_user_model()


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = Profile.get_cached_profile(user_id=request.user.id)
        user_location = UserLocation.objects.get(user=request.user)
        profile_form = ProfileForm(instance=profile)
        location_form = UserLocationForm(instance=user_location)
        return render(
            request,
            "accounts/profile.html",
            {"profile_form": profile_form, "location_form": location_form},
        )

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        user_location = UserLocation.objects.get(user=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        location_form = UserLocationForm(request.POST, instance=user_location)
        if profile_form.is_valid() and location_form.is_valid():
            profile_form.save()
            location_form.save()
            messages.success(request, _("Your profile has been updated."))
            return redirect("profile")
        else:
            messages.error(request, _("There was an error updating your profile."))
            return render(
                request,
                "accounts/profile.html",
                {"profile_form": profile_form, "location_form": location_form},
            )


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "accounts/profile_detail.html"


class WalletView(LoginRequiredMixin, View):
    def get(self, request):
        wallet = Wallet.objects.get(user=request.user)
        return render(request, "accounts/wallet.html", {"wallet": wallet})


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ["wallet", "value", "description"]
    template_name = "accounts/transaction_create.html"
    success_url = reverse_lazy("home")


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = "transactions"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(wallet__user=self.request.user)
