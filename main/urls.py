

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("editar/<int:id_user>/<int:id_anotacao>",
         views.editar,name="editar"),

    path("remover/<int:id_user>/<int:id_anotacao>",
         views.remover,name="remover"),

    path("anotacoes/<int:id_user>",
         views.anotacoes,name="anotacoes"),

    path("show/<int:id_user>/<int:id_anotacao>",
         views.show,name="show"),
]
