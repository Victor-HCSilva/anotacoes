from django.shortcuts import render
from .classes import (Agenda, Configs)
from django.http import HttpRequest
import datetime


def agenda(request: HttpRequest, id_user, ano=None, mes=None):
    agenda = Agenda(request)
    return agenda.agenda(id_user=id_user, ano=ano, mes=mes)


def configs(request: HttpRequest, id_user):
    configs = Configs(request=request)
    return configs.configs(id_user=id_user)
