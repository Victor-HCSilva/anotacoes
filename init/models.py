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
        ("Tarefa.","Tarefa"),
        ("Lembrete.","Lembrete"),
        ("Outro","Outro"),
    ]
    PRIORIDADES = [
        ("Mínima", "1"),
        ("Mediana","2"),
        ("Máxima", "3"),
    ]
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE
    )
    titulo = models.CharField(
        max_length=200
    )
    favorito = models.BooleanField(
        default=False
    )
    completo = models.BooleanField(
        default=False
    )
    anotacao = models.CharField(
        max_length=50000
    )
    prioridade = models.CharField(
        choices=PRIORIDADES,
        max_length=10
    )
    created_at = models.DateTimeField(("Data de Criação"), auto_now_add=True)
    updated_at = models.DateTimeField(("Data de Atualização"), auto_now=True)
    prazo_final = models.DateField()
    tag = models.CharField(
        choices=TAGS, max_length=13
    )
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


class Image(models.Model):
    img = models.ImageField(
        upload_to="imgs"
    )
    descricao = models.CharField(
        max_length=1000,
        default="Imagem sem descriçao"
    )
    titulo = models.CharField(
        max_length=1000, default="Sem titulo"
    )
    data_de_criacao = models.DateField(
        default=timezone.now
    )
    #Cada user tem um todo relacionado
    user = models.ForeignKey(
        Todo,
        on_delete=models.CASCADE,
        related_name="imagem"
    )
    observacao = models.CharField(max_length=1000, default="Sem observação")


    def __str__(self):
        return f"Titulo: {self.titulo} - {self.data_de_criacao}"
