from django.urls import path

from accounts import views

urlpatterns = [
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("wallet/", views.WalletView.as_view(), name="wallet"),
    path("ref/", views.ReferralLinkView.as_view(), name="referral"),
    path("invite/", views.ReferralInviteView.as_view(), name="referral_invite"),
    path("accounts/signup/", views.CustomSignupView.as_view(), name="account_signup"),
    path("tree/", views.ReferralTreeView.as_view(), name="referral_tree"),
]
