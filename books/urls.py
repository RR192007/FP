from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("account", views.checkloginstatus, name="checkloginstatus"),
    path("logout", views.logout_view, name="logout"),
    path("login", views.login_view, name="login_view"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout_view"),
    path("account/books/<int:id>", views.singlebook, name="singlebook"),
    path("account/books/<int:id>/borrow", views.borrow, name="borrow")
]