# Valores padrão, field e fields em dataclasses

from dataclasses import dataclass, field, fields


# Valores padrão podem ser definidos diretamente na declaração do campo ou
# usando field() para mais opções.
@dataclass
class Pessoa:
    nome: str = field(default="MISSING", repr=False)
    sobrenome: str = "Not sent"
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)
    # default_factory é usado para tipos mutáveis como listas


if __name__ == "__main__":
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)
