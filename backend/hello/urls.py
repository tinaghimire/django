from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("indexs", views.indexs, name="indexs"),
    path("greet", views.greet, name="greet"),
    path("<str:name>", views.callname, name="callname"),
]