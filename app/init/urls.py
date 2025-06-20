
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name="login"),
    path('main/<int:id_user>', views.main, name="main"),
    path('', views.logout_, name="logout"),
    path('welcome/<int:id_user>', views.welcome, name="welcome"),
]
