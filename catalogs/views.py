from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from catalogs.models import ProductCategory, Product


class CategoryListView(ListView):
    model = ProductCategory


class ProductListView(ListView):
    model = Product
