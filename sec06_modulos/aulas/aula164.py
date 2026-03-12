# Formatando datas

from datetime import datetime

fmt = "%d/%m/%Y %H:%M:%S"

data = datetime.strptime("2026-03-12 15:17:47", "%Y-%m-%d %H:%M:%S")
print(data.strftime("%d/%m/%Y"))
print(data.strftime("%d/%m/%Y %H:%M"))
print(data.strftime("%d/%m/%Y %H:%M:%S"))
print(data.strftime("%Y"))
print(data.strftime("%m"), data.month)  # str e int
print(data.strftime("%d"), data.day)
