# Dentro de utils.py - A VERSÃO CORRETA E SIMPLIFICADA
from datetime import date

# A função agora espera objetos do tipo 'date' diretamente.
# As anotações de tipo (data_inicial: date) são opcionais, mas uma boa prática.
def get_time_diff_days(data_inicial: date, data_final: date) -> int:
    """Calcula a diferença em dias entre dois objetos date."""

    # Não precisamos mais criar objetos date, eles já foram passados!
    # Apenas calculamos a diferença diretamente.
    diferenca = data_final - data_inicial

    return diferenca.days
