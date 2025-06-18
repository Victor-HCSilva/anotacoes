from django.forms import ModelForm
from .models import Colors, Agenda


class ColorForm(ModelForm):
    class Meta:
        model = Colors
        fields = ["cor"]


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = ["titulo","tipo_de_evento","descricao","dia_do_evento","importancia"]
