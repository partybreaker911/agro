from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Wallet
from deals.models import Deal


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home.html"

    def get(self, request):
        wallet = Wallet.objects.get(user=request.user)
        deals = Deal.objects.filter(user=request.user)
        context = {"wallet": wallet, "deals": deals}
        return render(request, self.template_name, context)


# def dashboard(request):
#     if request.user.is_authenticated:
#         return render(request, "dashboard/home.html")
#     else:
#         return redirect("account_login")
