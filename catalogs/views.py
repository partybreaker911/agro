from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from catalogs.models import ProductCategory, Product


class ProductCategoryView(ListView):
    model = ProductCategory
