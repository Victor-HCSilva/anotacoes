from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("agenda/<int:id_user>", views.agenda, name="agenda"),
    path("agenda/<int:id_user>/configs", views.configs, name="configs"),
]
