from django.urls import path

from catalogs import views

urlpatterns = [
    path("list/", views.CategoryListView.as_view(), name="category_list"),
    path("product/list/", views.ProductListView.as_view(), name="product_list"),
]
