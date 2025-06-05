from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

class Todo(models.Model):
    TAGS = [
        ("Universidade.","Universidade"),
        ("Casa","Casa"),
        ("Urgente.","Urgente"),
        ("Importante.","Importante"),
        ("Rotina.","Rotina"),
        ("Tarefa.","Tarefa"),
        ("Lembrete.","Lembrete"),
        ("Outro","Outro"),
    ]
    PRIORIDADES = [
        ("Mínima", "1"),
        ("Mediana","2"),
        ("Máxima", "3"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    anotacao = models.CharField(max_length=50000)
    prioridade = models.CharField(choices=PRIORIDADES, max_length=10)
    data_de_criacao = models.DateField(auto_now_add=True)
    prazo_final = models.DateField()
    tag = models.CharField(choices=TAGS, max_length=13)
    prazo_inicial = models.DateField(
        default=timezone.now,
        help_text=f'eg. {str(timezone.now().date())}'
    )
    prazo_inicial = models.DateField(
        default=timezone.now,

        help_text=f'eg. {str(timezone.now().date())}'
    )
    def __str__(self):
        return (f"Titulo: {self.titulo}")
