from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse
from app.anotacoes.models import Anotacao, Config
from app.anotacoes.forms import AnotacaoForm, ConfigForm



def anotacoes(request):
    return render(request, "text-anotacoes.html")


class AnotacaoListView(ListView):
    model = Anotacao
    template_name = "anotacao_list.html"
    context_object_name = "anotacoes"


class AnotacaoDetailView(DetailView):
    model = Anotacao
    template_name = "anotacao_detail.html"
    context_object_name = "anotacao"


class AnotacaoCreateView(CreateView):
    model = Anotacao
    form_class = AnotacaoForm
    template_name = "anotacao_form.html"
    success_url = reverse_lazy("anotacao_list")


class AnotacaoUpdateView(UpdateView):
    model = Anotacao
    form_class = AnotacaoForm
    template_name = "anotacao_form.html"
    success_url = reverse_lazy("anotacao_list")


class AnotacaoDeleteView(DeleteView):
    model = Anotacao
    template_name = "anotacao_confirm_delete.html"
    success_url = reverse_lazy("anotacao_list")


# ------------------------------
# CRUD para Configurações
# ------------------------------

class ConfigListView(ListView):
    model = Config
    template_name = "config_list.html"
    context_object_name = "configs"


class ConfigDetailView(DetailView):
    model = Config
    template_name = "config_detail.html"
    context_object_name = "config"


class ConfigCreateView(CreateView):
    model = Config
    form_class = ConfigForm
    template_name = "config_form.html"
    success_url = reverse_lazy("config_list")


class ConfigUpdateView(UpdateView):
    model = Config
    form_class = ConfigForm
    template_name = "config_form.html"
    success_url = reverse_lazy("config_list")


class ConfigDeleteView(DeleteView):
    model = Config
    template_name = "config_confirm_delete.html"
    success_url = reverse_lazy("config_list")
