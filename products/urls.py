from django.urls import path
from products import views

app_name = "products"

urlpatterns = [
    path("category/", views.CategoryView.as_view(), name="category"),
    path("category/list/", views.CategoryListView.as_view(), name="category-list"),
    path(
        "category/<uuid:pk>/",
        views.CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path(
        "product/<uuid:pk>/", views.ProductDetailView.as_view(), name="product-detail"
    ),
]
