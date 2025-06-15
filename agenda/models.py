from django.db import models
from django.contrib.auth.models import User
from solo.models import SingletonModel
from django.contrib.auth.models import User


class Colors(SingletonModel):
    COLORS = [
        ("blue", "blue"),
        ("green", "green"),
        ("red", "red"),
        ("white", "white")
    ]

    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE
    )

    cor = models.CharField(
        "Cor de Destaque",
        choices=COLORS,
        max_length=10,
        default="blue" # É uma boa ideia ter um valor padrão
    )

    def __str__(self):
        return self.cor

    class Meta:
        verbose_name = "Configuração de Cor"
