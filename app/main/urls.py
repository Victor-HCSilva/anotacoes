from django.contrib import admin
from django.urls import path
from . import views
from app.init import views as views_init
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    path('login/', views_init.CustomLoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='main:login'), name='logout'),

    path('main/<int:id_user>', views_init.main, name="main"),

    path('welcome/<int:id_user>', views_init.welcome, name="welcome"),

    path('sobre', views_init.sobre, name="sobre"),
#----------------------------------------------------
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

    path("not_found", views.not_found,name="404"),
]
