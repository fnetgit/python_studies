"""
NamedTuples: Tuplas Imutáveis com Nomes de Campos

Use quando precisar de:
• Registros simples (dados de DB, API responses, configs)
• Estruturas **leves e imutáveis**
• Acesso por **nome** (.campo) **OU** **índice** [0]

Vantagens vs dict:
- Validação de tipos (mypy)
- Mais rápido/legível
- Imutável

Vantagens vs class normal:
- Zero boilerplate
- Herda de tuple
"""

from typing import NamedTuple


# 1. FORMA MODERNA
class Carta(NamedTuple):
    valor: str
    naipe: str

    # Defaults funcionam direto
    # valor: str = "Ás"
    # naipe: str = "Espadas"


# 2. FORMA LEGACY (collections.namedtuple)
# from collections import namedtuple
# Carta = namedtuple('Carta', ['valor', 'naipe'], defaults=['Ás', 'Espadas'])


def main():
    # Criação flexível
    as_espadas = Carta("Ás", "Espadas")  # Posicional completo
    dois_paus = Carta(valor="2", naipe="Paus")  # Nomeado

    print(" ACESSO POR NOME E ÍNDICE ")
    print(f"Carta: {as_espadas}")
    print(f"Por nome: valor='{as_espadas.valor}', naipe='{as_espadas.naipe}'")
    print(f"Por índice: [0]='{as_espadas[0]}', [1]='{as_espadas[1]}'")

    print("\n METADATA ")
    print(f"Campos: {as_espadas._fields}")
    print(f"É tuple? {isinstance(as_espadas, tuple)}")
    # as_espadas.valor = "Rei"  # ERRO! Imutável

    print("\n DICT CONVERSION ")
    print(as_espadas._asdict())

    print("\n COMPARAÇÃO ")
    rei_copas = Carta("Rei", "Copas")
    print(f"{as_espadas} == {rei_copas}? {as_espadas == rei_copas}")


if __name__ == "__main__":
    main()
