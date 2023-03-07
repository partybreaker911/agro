from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from support.models import Ticket, Reply
from support.forms import TicketForm, ReplyForm


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy("ticket_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(user=user)


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    context_object_name = "tickets"
    form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super(TicketDetailView, self).get_context_data(**kwargs)
        context["form"] = ReplyForm(initial={"ticket": self.object})
        context["replyes"] = Reply.objects.filter(ticket=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(TicketDetailView, self).form_valid(form)
