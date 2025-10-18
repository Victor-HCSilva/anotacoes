from django.db import models
from app.init.models import Todo as Task
from app.anotacoes.config.colors import COLORS

class Anotacao(models.Model):
    title = models.CharField(max_length=100, default="Sem título")
    note = models.TextField(max_length=1000, default="Sem conteúdo")
    link = models.TextField(max_length=1000)

    # Tarefas associadas às anotações
    tasks = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Config(models.Model):
    text_color = models.CharField(max_length=20, choices=COLORS, default="black")
    link_color = models.CharField(max_length=20, choices=COLORS, default="blue")
    task_color = models.CharField(max_length=20, choices=COLORS, default="green")

    anotacao = models.ForeignKey(
        Anotacao,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Configuração para {self.anotacao.title}"
