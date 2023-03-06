from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.db import transaction

from accounts.models import Location
from products.models import Category, Product, ProductPrice
from products.forms import CategoryForm, ProductForm


class CategoryView(View):
    template_name = "products/category.html"

    def get(self, request, *args, **kwargs):
        category_id = kwargs.get("id")
        if category_id:
            category = Category.objects.get(id=category_id)
            form = CategoryForm(instance=category)
        else:
            form = CategoryForm()
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        category_id = kwargs.get("id")
        if category_id:
            category = Category.objects.get(id=category_id)
            form = CategoryForm(request.POST, instance=category)
        else:
            form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
        else:
            context = {
                "form": form,
            }
            return redirect(request, self.template_name, context)


class CategoryDetailView(DetailView):
    model = Category
    template_name = "products/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context["products"] = category.product_set.all()
        return context


class CategoryListView(View):
    template_name = "products/category_list.html"

    def get(self, request, *args, **kwargs):
        categoryes = Category.objects.all()
        context = {
            "categoryes": categoryes,
        }
        return render(request, self.template_name, context)


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    TODO: need to design order model, and delete this!
    """

    model = Product
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        user = self.request.user
        location = user.profile.location
        try:
            product_price = ProductPrice.objects.get(product=product, location=location)
        except ProductPrice.DoesNotExist:
            product_price = None
        context["product_price"] = product_price
        return context

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        user = self.request.user
        location = user.profile.location
        product_price = ProductPrice.objects.filter(
            product=product, location=location
        ).first()
        if not product_price:
            messages.error(
                request, _("This product is not available in your location.")
            )
            return self.get(request, *args, **kwargs)
        if user.wallet.balance < product_price.price:
            messages.error(
                request, _("You don't have enough points to purchase this product.")
            )
            return self.get(request, *args, **kwargs)
        with transaction.atomic():
            user.wallet.balance -= product_price.price
            user.wallet.save()
            product.sold_count += 1
            product.save()
        messages.success(
            request, _("Congratulations, you have successfully purchased this product.")
        )
        return redirect("products:product-detail", pk=product.pk)
