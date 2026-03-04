from datetime import datetime, timezone
from zoneinfo import ZoneInfo  # Nativo a partir do Python 3.9

agora_fortaleza = datetime.now(ZoneInfo("America/Fortaleza"))
print(agora_fortaleza)

data_ny = datetime(2026, 3, 3, 19, 6, tzinfo=ZoneInfo("America/New_York"))
print(data_ny)

# converte a data de NY para o fuso de Tokyo
data_tokyo = data_ny.astimezone(ZoneInfo("Asia/Tokyo"))
print(data_tokyo)

# Converte timestamp Unix (segundos desde 1970-01-01 00:00:00 UTC) para datetime
print(datetime.fromtimestamp(1, tz=ZoneInfo("UTC")))

# Mesma coisa mas usando timezone.utc do módulo datetime
print(datetime.fromtimestamp(1, tz=timezone.utc))
