from django.contrib import admin
from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path("<int:id_user>", views.agenda, name="agenda"),
    path("<int:id_user>", views.eventos_, name="eventos"),
    path("<int:id_user>/configs", views.configs_, name="configs"),
    path("cancelar_evento/<int:id_user>/<int:id_event>", views.delete_event_, name="deletar_evento"),
    path("editar_evento/<int:id_user>/<int:id_event>", views.edit_event, name="editar_evento"),
]
