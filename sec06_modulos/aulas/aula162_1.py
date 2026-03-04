# Datas

from datetime import datetime

data = datetime(2026, 3, 3, 17, 30)
print(data)

data_str_formt = "%Y-%m-%d %H:%M:%S"
# Poderia ser / ou outro separador, mas tem que ser o mesmo do data_str
data_str = "2026-03-03 17:33:20"
data_2 = datetime.strptime(data_str, data_str_formt)
print(data_2)

print(datetime.now(), "\n")

# para timezones precisamos do modulo pytz e types-pytz (pra tipagem)
from pytz import timezone

# Quando se criaa data manualmente usa tzinfo
# Em funções que geram data automaticamente, usa-se o parâmetro tz

print(datetime.now(timezone("America/Fortaleza")))
print(datetime(2026, 3, 3, 19, 6, tzinfo=timezone("America/New_York")))

print(data.timestamp())  # timestamp é o número de segundos desde 1 de janeiro de 1970

# converte o timestamp de volta para um objeto datetime
print(datetime.fromtimestamp(data.timestamp()))

print(datetime.fromtimestamp(1))  # 1 segundo depois de 1 de janeiro de 1970,
# porém só vai mostrar isso se o fuso for timezone("UTC")
print(datetime.fromtimestamp(1, tz=timezone("UTC")))
