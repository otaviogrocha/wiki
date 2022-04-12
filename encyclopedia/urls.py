from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("/newEntry", views.newEntry, name="newEntry"),
    path("<str:entry>/edit", views.edit, name="edit"),
    path("/search", views.search, name="search"),
    path("/random", views.random, name="random")
]
