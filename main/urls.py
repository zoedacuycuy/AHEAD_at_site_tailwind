from django.urls import path

from . import views

urlpatterns = [
    path("", views.LandingPage, name="LandingPage"),
    path("about/", views.About, name="About"),
]