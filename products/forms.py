from django import forms
from products.models import Category, Product
from dal import autocomplete


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            "name",
            "parent",
        )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "name")
