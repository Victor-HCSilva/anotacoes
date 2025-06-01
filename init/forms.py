from django.forms import ModelForm, Textarea
from .models import (User, Todo)


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["titulo","anotacao","prioridade","tag"]
        widgets = {
            "anotacao": Textarea(attrs={"cols": 80, "rows": 20}),
        }
        labels = {
            "anotacao": "Anotação",
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        labels = {
            "username": "Nome:",
            "password":"Senha:"
        }
