from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginview, name="login"),
    path("logout/", views.logoutview, name="logout"),
    path("register/", views.register, name="register"),
    path("", views.home, name="home"),
]