# Comparando datas - timedelta

from datetime import datetime, timedelta

fmt = "%d/%m/%Y %H:%M:%S"
data_inicio = datetime.strptime("13/10/2005 12:00:00", fmt)
data_fim = datetime.strptime("12/03/2026 14:50:00", fmt)

print(data_inicio == data_fim)

delta = data_fim - data_inicio
print(delta)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

delta_2 = timedelta(days=10)
print(data_inicio + delta_2)

# uv add python-dateutil types-python-dateutil
from dateutil.relativedelta import relativedelta

# aceita meses e anos, faz o cálculo considerando os dias de cada mês e anos bissextos
print(data_inicio + relativedelta(years=10, months=2))

delta_3 = relativedelta(years=10, months=2)
print(delta_3)

print(delta_3.days, delta_3.months, delta_3.years)
