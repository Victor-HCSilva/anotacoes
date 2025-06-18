import calendar
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ColorForm
from django.contrib.auth.models import User
from .models import Colors, Agenda
from .forms import AgendaForm
from .utils import get_days


class Agenda:
    def __init__(self, request):
        self.request = request

    def agenda(self, id_user, ano=None, mes=None):
        form = AgendaForm(self.request.POST)

        if self.request.method == "POST":
            if form.is_valid():
                agenda = form.save(commit=False)
                agenda.user = user
                print("User:", config.user)
                agenda.save()
            else:
                print("Erros:",form.errors)

        agora = datetime.now()
        ano = ano or agora.year
        mes = mes or agora.month
        cal = calendar.Calendar(firstweekday=6)
        mes_dias = cal.monthdayscalendar(ano, mes)
        nome_mes = calendar.month_name[mes]
        hoje = datetime.now()
        dia_do_mes = hoje.day
        user = get_object_or_404(User, id=id_user)
        cor_de_destaque = Colors.objects.filter(user=user).first()
        eventos = Agenda.objects.all("")

        context = {
            'ano': ano,
            'mes': mes,
            'nome_mes': nome_mes,
            'dias_semana': ['Dom', 'Seg', 'Ter',
                            'Qua', 'Qui', 'Sex', 'Sáb'
                        ],
            'mes_dias': mes_dias,
            'id_user': id_user,
            "dia_atual":dia_do_mes,
            "cor_de_destaque":cor_de_destaque,
        }

        return render(self.request, "agenda.html", context)


class Configs:
    def __init__(self, request: HttpRequest):
        self.request = request


    def configs(self, id_user: int):
        form = ColorForm(self.request.POST)
        user = get_object_or_404(User, id=id_user)
        context = {
            "nada":"nada",
            "cor_de_destaque":form,
            "user":user,
        }


        if self.request.method == "POST":
            if form.is_valid():
                config = form.save(commit=False)
                config.user = user
                print("User:",config.user)
                config.save()
                return redirect("agenda", id_user=id_user)
        else:
            print("Erros",form.errors)

        return render(self.request, "configs.html", context)
