from django.urls import path
from . import views

urlpatterns = [
    path("", views.year, name = "year")
]