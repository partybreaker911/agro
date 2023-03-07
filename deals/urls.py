from django.urls import path

from deals import views

urlpatterns = [
    path("list/", views.DealListView.as_view(), name="deal_list"),
    path("create/", views.DealCreateView.as_view(), name="deal_create"),
]
