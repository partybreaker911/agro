from django.urls import path

from deals import views

urlpatterns = [
    path("list/", views.DealListView.as_view(), name="deal_list"),
    path("create/", views.DealCreateView.as_view(), name="deal_create"),
    path("<uuid:pk>/update/", views.DealUpdateView.as_view(), name="deal_update"),
    path("<uuid:pk>/detail/", views.DealDetailView.as_view(), name="deal_detail"),
    path("<uuid:pk>/delete/", views.DealDeleteView.as_view(), name="deal_delete"),
]
