from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from support.models import Ticket
from support.forms import TicketForm


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(user=user)
