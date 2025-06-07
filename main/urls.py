

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

    path("apagar_imagem/<int:id_user>/<int:id_anotacao>/<int:id_imagem>",
         views.apagar_imagem,name="apagar_imagem"),

    path("editar_descricao/<int:id_user>/<int:id_anotacao>/<int:id_imagem>",
         views.editar_descricao,name="editar_descricao"),
]
