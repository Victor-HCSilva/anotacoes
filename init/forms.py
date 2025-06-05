from django.forms import ModelForm, Textarea
from .models import (User, Todo)
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["titulo","anotacao","prioridade","tag","prazo_inicial", "prazo_final"]
        widgets = {
            "anotacao": Textarea(attrs={"cols": 80, "rows": 20}),

            'prazo_final': forms.DateInput(
                attrs={
                    'type': 'date', # Isso usará o widget de data nativo do navegador
                    'class': 'form-control', # Exemplo de classe CSS (Bootstrap)
                    # 'placeholder': 'AAAA-MM-DD' # Se não usar type='date'
                },
                format='%Y-%m-%d' # Formato que o widget espera/envia (ISO 8601 é bom para type='date')
            ),

            'prazo_inicial': forms.DateInput(
                attrs={
                    'type': 'date', # Isso usará o widget de data nativo do navegador
                    'class': 'form-control', # Exemplo de classe CSS (Bootstrap)
                    # 'placeholder': 'AAAA-MM-DD' # Se não usar type='date'
                },
                format='%Y-%m-%d' # Formato que o widget espera/envia (ISO 8601 é bom para type='date')
            ),
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
