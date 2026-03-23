# os.listdir - listar arquivos e pastas em um diretório

import os

caminho = os.path.join("sec06_modulos", "aulas")

for item in os.listdir(caminho):
    print(item)

print("-" * 20)

# Pathlib - mais a partir do Python 3.4
from pathlib import Path

caminho = Path("sec06_modulos") / "aulas"

for item in caminho.iterdir():
    print(item.name)
