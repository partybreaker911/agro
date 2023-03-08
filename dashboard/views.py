from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Wallet, Profile
from invitations.models import Invitation
from deals.models import Deal


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home.html"

    def get(self, request):
        wallet = Wallet.objects.get(user=request.user)
        deals = Deal.objects.filter(user=request.user)
        invited = Invitation.objects.filter(inviter=request.user).values("email")
        invited_users = Profile.objects.filter(user__email__in=invited)
        context = {
            "wallet": wallet,
            "deals": deals,
            "invited": invited,
            "invited_users": invited_users,
        }
        return render(request, self.template_name, context)
