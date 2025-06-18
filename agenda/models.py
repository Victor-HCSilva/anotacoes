from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Classe renomeada para ser mais descritiva
class Colors(models.Model):
    class Cor(models.TextChoices):
        AZUL = "blue", "Azul"
        VERDE = "green", "Verde"
        VERMELHO = "red", "Vermelho"
        BRANCO = "white", "Branco"

    # OneToOneField garante que cada usuário tenha apenas uma configuração
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True, # Torna o usuário a chave primária da tabela
    )
    cor = models.CharField(
        "Cor de destaque",
        max_length=10,
        choices=Cor.choices,
        default=Cor.AZUL
    )

    def __str__(self):
        return f"Configuração de {self.user.username}"


class Agenda(models.Model):
    # Usando a forma moderna e mais clara de definir choices
    class Prioridade(models.TextChoices):
        MINIMA = "1", "Mínima"
        MEDIANA = "2", "Mediana"
        MAXIMA = "3", "Máxima"

    class TipoEvento(models.TextChoices):
        PROVA = "Prova", "Prova"
        ATIVIDADE = "Atividade", "Atividade"
        TAREFA = "Tarefa", "Tarefa"
        IMPORTANTE = "Importante", "Importante"
        LEMBRETE = "Lembrete", "Lembrete"
        PASSEIO = "Passeio", "Passeio"
        OUTRO = "Outro", "Outro"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )
    titulo = models.CharField("Título", max_length=200)
    descricao = models.TextField("Descrição", blank=True, default="")
    tipo_de_evento = models.CharField(
        "Tipo de Evento",
        max_length=20,
        choices=TipoEvento.choices,
        default=TipoEvento.LEMBRETE
    )
    importancia = models.CharField(
        "Importância",
        max_length=2,
        choices=Prioridade.choices,
        default=Prioridade.MINIMA
    )
    dia_do_evento = models.DateTimeField("Data do evento", default=timezone.now)
    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)
    updated_at = models.DateTimeField("Data de Atualização", auto_now=True)

    class Meta:
        # Boa prática: ordenar os eventos pela data
        ordering = ['dia_do_evento']

    def __str__(self):
        # Correção: usar self. e formatar a data
        return f"{self.titulo} ({self.user.username}) - {self.dia_do_evento.strftime('%d/%m/%Y')}"
