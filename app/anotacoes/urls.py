from django.urls import path
from app.anotacoes.views import anotacoes
from django.urls import path
from app.anotacoes.views import (
    AnotacaoListView, AnotacaoDetailView, AnotacaoCreateView,
    AnotacaoUpdateView, AnotacaoDeleteView,
    ConfigListView, ConfigDetailView, ConfigCreateView,
    ConfigUpdateView, ConfigDeleteView
)


urlpatterns = [
    # ------------------------------
    # CRUD para Anotações
    # ------------------------------
    path("anotacoes/", AnotacaoListView.as_view(), name="anotacao_list"),
    path("anotacoes/novo/", AnotacaoCreateView.as_view(), name="anotacao_create"),
    path("anotacoes/<int:pk>/", AnotacaoDetailView.as_view(), name="anotacao_detail"),
    path("anotacoes/<int:pk>/editar/", AnotacaoUpdateView.as_view(), name="anotacao_update"),
    path("anotacoes/<int:pk>/deletar/", AnotacaoDeleteView.as_view(), name="anotacao_delete"),

    # ------------------------------
    # CRUD para Configurações
    # ------------------------------
    path("configs/", ConfigListView.as_view(), name="config_list"),
    path("configs/novo/", ConfigCreateView.as_view(), name="config_create"),
    path("configs/<int:pk>/", ConfigDetailView.as_view(), name="config_detail"),
    path("configs/<int:pk>/editar/", ConfigUpdateView.as_view(), name="config_update"),
    path("configs/<int:pk>/deletar/", ConfigDeleteView.as_view(), name="config_delete"),
]
