
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name="login"),
    path('main/<int:id_user>', views.main, name="main"),
    path('', views.logout, name="logout"),
]
