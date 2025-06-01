from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    TAGS = [
        ("Esc.","Universidade"),
        ("Casa","Casa"),
        ("Urg.","Urgente"),
        ("Imp.","Importante"),
        ("Rot.","Rotina"),
        ("Tar.","Tarefa"),
        ("Lem.","Lembrete"),
        ("Any","Outro"),
    ]
    PRIORIDADES = [
        ("Mínima", "1"),
        ("Mediana","2"),
        ("Máxima", "3"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    anotacao = models.CharField(max_length=3000)
    prioridade = models.CharField(choices=PRIORIDADES, max_length=10)
    data_de_criacao = models.DateField(auto_now_add=True)
    tag = models.CharField(choices=TAGS, max_length=10)

    def __str__(self):
        return (f"Titulo: {self.titulo}")
