from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy

from deals.models import Deal
from deals.forms import DealForm


class DealListView(LoginRequiredMixin, ListView):
    model = Deal
    template_name = "deal/deal_list.html"
    context_object_name = "deals"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset.all()
        else:
            return queryset.filter(user=self.request.user)


class DealCreateView(LoginRequiredMixin, CreateView):
    model = Deal
    form_class = DealForm
    template_name = "deal/deal_create.html"
    success_url = reverse_lazy("deal_list")

    def form_valid(self, form):
        deal = form.save(commit=False)
        form.instance.user = self.request.user
        if self.request.user.is_staff:
            deal.approved = True
        deal.save()
        return super().form_valid(form)


class DealDetailView(LoginRequiredMixin, DetailView):
    model = Deal
    template_name = "deal/deal_detail.html"


class DealDeleteView(LoginRequiredMixin, DeleteView):
    model = Deal


class DealUpdateView(LoginRequiredMixin, UpdateView):
    model = Deal
    fields = ["product", "quantity", "type", "approved"]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            del form.fields["approved"]
        return form
