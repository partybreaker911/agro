from django.urls import path

from accounts import views

urlpatterns = [
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path(
        "profile/<uuid:pk>/", views.ProfileDetailView.as_view(), name="profile_detail"
    ),
    path("wallet/", views.WalletView.as_view(), name="wallet"),
]
