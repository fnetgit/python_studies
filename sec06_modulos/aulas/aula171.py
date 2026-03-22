# os.walk

# permite percorrer uma estrutura de diretórios de forma recursiva
# retorna uma tupla com o caminho do diretório, os subdiretórios e os arquivos
import os

caminho = os.path.join("sec06_modulos", "aulas")
for root, dirs, files in os.walk(caminho):
    print(f"Diretório: {root}")
    print(f"Subdiretórios: {dirs}")
    print(f"Arquivos: {files}")

# com pathlib
from pathlib import Path

caminho = Path("sec06_modulos") / "aulas"

# rglob("*") percorre todas as subpastas e arquivos
for item in caminho.rglob("*"):
    tipo = "Diretório" if item.is_dir() else "Arquivo"
    print(f"{tipo}: {item}")
