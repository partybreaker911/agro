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

from deals.models import Deal, ProductPrice
from deals.forms import DealForm


class DealListView(LoginRequiredMixin, ListView):
    """
    TODO: Добавить поиск по таблице
    """

    model = Deal
    template_name = "deal/deal_list.html"
    context_object_name = "deals"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset.all()
        else:
            return queryset.filter(user=self.request.user)


class DealCreateView(LoginRequiredMixin, CreateView):
    model = Deal
    form_class = DealForm
    # fields = ["product", "type", "quantity"]
    template_name = "deal/deal_create.html"
    success_url = reverse_lazy("deal_list")

    def form_valid(self, form):
        """
        TODO: Надо добавить выбор продуктов только тех которые есть в данном регионе и у них есть устновленная цена
        """
        # deal = form.save(commit=False)
        form.instance.user = self.request.user
        product = form.cleaned_data["product"]
        user_location = self.request.user.userlocation.location
        price = (
            ProductPrice.objects.filter(product=product, location=user_location)
            .first()
            .price
        )
        quantity = form.cleaned_data["quantity"]
        total_price = float(price) * float(quantity)
        self.object = form.save(commit=False)
        self.object.total_price = total_price
        self.object.save()
        if self.request.user.is_staff:
            pass
            # deal.approved = True
        # deal.save()
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


class ProductPriceListView(LoginRequiredMixin, ListView):
    model = ProductPrice
    template_name = "deal/product_price_list.html"
    paginate_by = 10
