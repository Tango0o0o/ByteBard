from django.urls import path
from . import account_views, views

urlpatterns = [
    # user account stuff
    path("login/", account_views.loginview, name="login"),
    path("logout/", account_views.logoutview, name="logout"),
    path("register/", account_views.register, name="register"),
    path("profile/", account_views.profile, name="profile"),

    path("", views.home, name="home"),
]