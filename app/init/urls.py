
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path("create-account", views.create_account, name="create_account")
]
