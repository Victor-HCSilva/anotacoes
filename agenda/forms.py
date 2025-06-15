from django.forms import ModelForm
from .models import Colors


class ColorForm(ModelForm):
    class Meta:
        model = Colors
        fields = ["cor"]
