import calendar
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ColorForm
from django.contrib.auth.models import User
from .models import Colors, AgendaModel
from .forms import AgendaForm
from collections import defaultdict


class Agenda:
    def __init__(self, request):
        self.request = request

    def agenda(self, id_user, ano=None, mes=None):
        if self.request.user.id != id_user:
            return redirect('login')

        form = AgendaForm(self.request.POST)
        user = get_object_or_404(User, id=id_user)

        if form.is_valid():
            if self.request.method == "POST":
                agenda = form.save(commit=False)
                agenda.user = user
                print("User:", agenda.user)
                agenda.save()
                return redirect("agenda", id_user=id_user)
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
        cor_obj = Colors.objects.filter(user=user).first()
        cor_de_destaque = cor_obj.cor_de_destaque if cor_obj else "#808080" # Usa cinza se não houver cor
        eventos_do_mes = AgendaModel.objects.filter(
            user=user, dia_do_evento__year=ano,
            dia_do_evento__month=mes
        )
        eventos_por_dia = defaultdict(list)

        for evento in eventos_do_mes:
            eventos_por_dia[evento.dia_do_evento.day].append(evento.titulo)

        context = {
            'ano': ano,
            'mes': mes,
            'nome_mes': nome_mes,
            'dias_semana': ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'],
            'mes_dias': mes_dias,
            'id_user': id_user,
            "dia_atual": dia_do_mes,
            "cor_de_destaque": cor_de_destaque,
            "eventos_do_mes": eventos_do_mes,  # Para a lista no final da página
            "eventos_por_dia": dict(eventos_por_dia), # O dicionário para o calendário
            "form": form,
        }

        return render(self.request, "agenda.html", context)


class Configs:
    def __init__(self, request: HttpRequest):
        self.request = request


    def configs(self, id_user: int):
        #Caso não seja o mesmo usuario
        if self.request.user.id != id_user:
            return redirect('login')

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


class DeleteOrEditEvent():
    def __init__(self, request: HttpRequest):
        self.request = request


    def delete_event(self, id_user: int, id_event):
        #Caso não seja o mesmo usuario
        if self.request.user.id != id_user:
            return redirect('login')

        evento = get_object_or_404(AgendaModel, id=id_event)
        user = get_object_or_404(User, id=id_user)
        context = {
            "user":user,
            "evento":evento,
        }

        if self.request.method == "POST":
            evento.delete()
            return redirect("agenda", id_user=id_user)

        return render(self.request, "delete_event.html", context)


    def edit_event(self, id_user: int, id_event: int):
        #Caso não seja o mesmo usuario
        if self.request.user.id != id_user:
            return redirect('login')

        evento = get_object_or_404(AgendaModel, id=id_event)
        user = get_object_or_404(User, id=id_user)

        if self.request.method == "POST":
            form = AgendaForm(self.request.POST, instance=evento)
            if form.is_valid():
                form.save()
            else:
                print("erros",form.errors)

            return redirect("agenda", id_user=id_user)

        form = AgendaForm(instance=evento)
        context = {
            "nada":"nada",
            "form":form,
            "user":user,
        }

        return render(self.request, "edit.html", context)
