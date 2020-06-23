from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("account", views.checkloginstatus, name="checkloginstatus"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login_view"),
    path("register", views.register, name="register")
]