from django.urls import path

from catalogs import views

urlpatterns = [
    path("list/", views.ProductCategoryView.as_view(), name="category_list"),
]
