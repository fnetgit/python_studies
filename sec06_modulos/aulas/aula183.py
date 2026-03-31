# string.Template para substituir variáveis em textos

# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros

import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / "aula183.txt"

locale.setlocale(locale.LC_ALL, "")


def converte_para_brl(numero: float) -> str:
    brl = locale.currency(numero, grouping=True)
    return brl


data = datetime(2026, 3, 30)
dados = dict(
    nome="João",
    valor=converte_para_brl(1_234_456),
    data=data.strftime("%d/%m/%Y"),
    empresa="F. N.",
    telefone="+55 (86) 7890-5432",
)

# O delimitador padrão é o $, mas pode ser alterado criando uma subclasse de Template
# class MyTemplate(string.Template):
#     delimiter = "%"


with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
