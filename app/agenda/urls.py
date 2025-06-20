from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("agenda/<int:id_user>", views.agenda, name="agenda"),
    path("agenda/<int:id_user>/configs", views.configs_, name="configs"),
    path("agenda/cancelar_evento/<int:id_user>/<int:id_event>", views.delete_event_, name="deletar_evento"),
    path("agenda/editar_evento/<int:id_user>/<int:id_event>", views.edit_event, name="editar_evento"),
]
