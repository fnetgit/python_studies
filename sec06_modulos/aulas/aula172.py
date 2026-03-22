# getsize() e stat()

import os
from datetime import datetime

caminho_os = os.path.join("sec06_modulos", "aulas", "aula170.py")

estatisticas = os.stat(caminho_os)
tamanho = estatisticas.st_size
data_formatada = datetime.fromtimestamp(estatisticas.st_mtime).strftime(
    "%Y-%m-%d %H:%M:%S"
)

print(f"Tamanho: {tamanho} bytes")
print(f"Última modificação: {data_formatada}")

print("-" * 20)

# com pathlib
from pathlib import Path

caminho_pl = Path("sec06_modulos") / "aulas" / "aula170.py"

info = caminho_pl.stat()
tamanho_pl = info.st_size
ultima_mod_pl = datetime.fromtimestamp(info.st_mtime).strftime("%Y-%m-%d %H:%M:%S")

print(f"Tamanho: {tamanho_pl} bytes")
print(f"Última modificação: {ultima_mod_pl}")
