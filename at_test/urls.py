from django.urls import path

from . import views

urlpatterns = [
    path("starttest/", views.StartTest, name="StartTest"),
    path("<int:item>/", views.Test, name="Test"),
]