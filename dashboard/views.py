from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from accounts.models import Wallet, Profile
from invitations.models import Invitation
from deals.models import Deal

User = get_user_model()


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home.html"

    def get(self, request):
        wallet = Wallet.objects.get(user=request.user)
        deals = Deal.objects.filter(user=request.user)
        deal_count = Deal.objects.filter(user=request.user).count()
        invited = Invitation.objects.filter(inviter=request.user).values("email")
        invited_users = Profile.objects.filter(user__email__in=invited)
        invitations_send = User.objects.filter(invitation__isnull=False).count()
        context = {
            "wallet": wallet,
            "deals": deals,
            "deal_count": deal_count,
            "invited": invited,
            "invited_users": invited_users,
            "invitations_send": invitations_send,
        }
        return render(request, self.template_name, context)
