# csv.reader e csv.DictReader - ler o csv em formato de lista ou dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "aula179.csv"

with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha["Nome"], linha["Idade"], linha["Endereço"])

print()

with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
