from datetime import date
# 1. Obtenha a data de hoje
hoje = date.today()

# 2. Defina a data futura
data_futura = date(2025, 6, 17)

# 3. Calcule a diferença (o resultado é um objeto 'timedelta')
diferenca = data_futura - hoje

# 4. Imprima o número de dias a partir do objeto timedelta
print(f"Faltam {diferenca.days} dias até 17/06/2025.")
