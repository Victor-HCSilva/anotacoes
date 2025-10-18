
from django import forms
from app.anotacao.models import Anotacao, Config


class AnotacaoForm(forms.ModelForm):
    class Meta:
        model = Anotacao
        fields = ["title", "note", "link", "tasks"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título"}),
            "note": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Escreva sua anotação..."}),
            "link": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://..."}),
            "tasks": forms.Select(attrs={"class": "form-select"}),
        }


class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = ["text_color", "link_color", "task_color", "anotacao"]
        widgets = {
            "text_color": forms.Select(attrs={"class": "form-select"}),
            "link_color": forms.Select(attrs={"class": "form-select"}),
            "task_color": forms.Select(attrs={"class": "form-select"}),
            "anotacao": forms.Select(attrs={"class": "form-select"}),
        }
