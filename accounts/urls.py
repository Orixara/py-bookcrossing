from django.urls import path, include

from accounts.views import (
    SignUpView,
    ActivateAccountView,
    ProfileView,
    ProfileUpdateView,
)

app_name = "accounts"


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="sign-up"),
    path("activate/<str:uid>/<str:token>/", ActivateAccountView.as_view(), name="activate"),
    path("", include("django.contrib.auth.urls")),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile-edit"),

]