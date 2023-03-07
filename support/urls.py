from django.urls import path

from support import views

urlpatterns = [
    path("create/", views.TicketCreateView.as_view(), name="ticket_create"),
    path("list/", views.TicketListView.as_view(), name="ticket_list"),
]
